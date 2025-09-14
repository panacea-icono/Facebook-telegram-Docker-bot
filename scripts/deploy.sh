#!/bin/bash
# Deploy Rasa multicanal bot

set -euo pipefail

echo "🚀 Deploying Rasa multicanal bot..."

# Check if .env file exists and is properly configured
if [ ! -f ".env" ]; then
    echo "❌ Error: .env file not found. Please create it from .env.example and configure your tokens."
    exit 1
fi

# Validate that essential tokens are configured
source .env
if [ -z "${TELEGRAM_BOT_TOKEN:-}" ] || [ "${TELEGRAM_BOT_TOKEN}" = "TU_TELEGRAM_TOKEN" ]; then
    echo "❌ Error: TELEGRAM_BOT_TOKEN is not configured in .env"
    exit 1
fi

if [ -z "${FB_PAGE_TOKEN:-}" ] || [ "${FB_PAGE_TOKEN}" = "TU_FB_PAGE_TOKEN" ]; then
    echo "❌ Error: FB_PAGE_TOKEN is not configured in .env"
    exit 1
fi

echo "✅ Environment variables validated"

# Build and train model if needed
if [ ! -d "models" ] || [ -z "$(ls -A models 2>/dev/null)" ]; then
    echo "🎓 Training model for deployment..."
    ./scripts/train.sh
fi

# Build Docker images
echo "🏗️  Building Docker images..."
docker compose build --no-cache

# Start services in production mode
echo "🚀 Starting services..."
docker compose up -d --force-recreate

# Wait for services to be healthy
echo "⏳ Waiting for services to be ready..."
sleep 15

# Check service health
echo "🏥 Checking service health..."
if ! docker compose ps | grep -q "healthy"; then
    echo "⚠️  Some services may not be healthy. Checking logs..."
    docker compose logs --tail=50
fi

# Display deployment information
echo ""
echo "🎉 Deployment completed!"
echo ""
echo "📊 Service status:"
docker compose ps

echo ""
echo "🌐 Your bot is available at:"
echo "  • Rasa API: http://localhost:5005"
echo "  • Health check: http://localhost:5005/status"
echo ""
echo "📱 Configure webhooks using:"
echo "  ./scripts/set-webhook.sh"
echo ""
echo "📋 Useful commands:"
echo "  • View logs: docker compose logs -f"
echo "  • Stop deployment: ./scripts/down.sh"
echo "  • Clean deployment: ./scripts/clean.sh"