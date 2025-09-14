#!/bin/bash
# Start Rasa services using Docker Compose

set -euo pipefail

echo "🚀 Starting Rasa multicanal bot services..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found. Creating from .env.example..."
    cp .env.example .env
    echo "❗ Please edit .env with your actual tokens before the bot will work properly."
fi

# Check if model exists
if [ ! -d "models" ] || [ -z "$(ls -A models 2>/dev/null)" ]; then
    echo "⚠️  No trained model found. Training model first..."
    ./scripts/train.sh
fi

# Start services
echo "🔧 Starting Docker services..."
docker compose up -d

# Wait for services to be healthy
echo "⏳ Waiting for services to be ready..."
sleep 10

# Check service status
echo "📊 Service status:"
docker compose ps

echo ""
echo "✅ Rasa multicanal bot is running!"
echo ""
echo "🌐 Endpoints available:"
echo "  • Rasa API: http://localhost:5005"
echo "  • Actions server: http://localhost:5055"
echo ""
echo "📱 Webhook URLs for channels:"
echo "  • Telegram: http://your-domain.com/webhooks/telegram/webhook"
echo "  • Facebook: http://your-domain.com/webhooks/facebook/webhook"
echo ""
echo "To stop services, run: ./scripts/down.sh"
echo "To view logs, run: docker compose logs -f"