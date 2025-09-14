#!/bin/bash
# Set webhooks for Telegram and Facebook channels

set -euo pipefail

echo "🔗 Setting up webhooks for Telegram and Facebook..."

# Load environment variables
if [ ! -f ".env" ]; then
    echo "❌ Error: .env file not found. Please create it from .env.example"
    exit 1
fi

source .env

# Get the public URL (you might want to modify this for your deployment)
if [ -t 0 ]; then
    read -p "🌐 Enter your public domain/URL (e.g., https://yourdomain.com): " PUBLIC_URL
else
    PUBLIC_URL="${PUBLIC_URL:-${1:-}}"
    if [ -z "$PUBLIC_URL" ]; then
        echo "❌ Error: Public URL is required. Pass as first argument in non-interactive mode."
        echo "Usage: $0 <public_url>"
        exit 1
    fi
fi

if [ -z "$PUBLIC_URL" ]; then
    echo "❌ Error: Public URL is required"
    exit 1
fi

# Remove trailing slash
PUBLIC_URL=${PUBLIC_URL%/}

echo "🤖 Setting up Telegram webhook..."

if [ -z "${TELEGRAM_BOT_TOKEN:-}" ] || [ "${TELEGRAM_BOT_TOKEN}" = "TU_TELEGRAM_TOKEN" ]; then
    echo "⚠️  Warning: TELEGRAM_BOT_TOKEN not configured. Skipping Telegram webhook."
else
    TELEGRAM_WEBHOOK_URL="${PUBLIC_URL}/webhooks/telegram/webhook"
    
    echo "📤 Setting Telegram webhook to: $TELEGRAM_WEBHOOK_URL"
    
    # Set Telegram webhook
    curl -X POST \
        "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/setWebhook" \
        -H "Content-Type: application/json" \
        -d "{\"url\":\"${TELEGRAM_WEBHOOK_URL}\"}"
    
    echo ""
    echo "✅ Telegram webhook configured!"
    
    # Get webhook info
    echo "📋 Telegram webhook info:"
    curl -s "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/getWebhookInfo" | python3 -m json.tool || echo "Failed to get webhook info"
fi

echo ""
echo "📘 Setting up Facebook webhook..."

if [ -z "${FB_VERIFY_TOKEN:-}" ] || [ "${FB_VERIFY_TOKEN}" = "palabra-secreta" ]; then
    echo "⚠️  Warning: FB_VERIFY_TOKEN not configured properly."
fi

if [ -z "${FB_PAGE_TOKEN:-}" ] || [ "${FB_PAGE_TOKEN}" = "TU_FB_PAGE_TOKEN" ]; then
    echo "⚠️  Warning: FB_PAGE_TOKEN not configured. Please set up Facebook webhook manually."
else
    FB_WEBHOOK_URL="${PUBLIC_URL}/webhooks/facebook/webhook"
    echo "📤 Facebook webhook URL: $FB_WEBHOOK_URL"
    echo "🔑 Facebook verify token: ${FB_VERIFY_TOKEN}"
    
    echo ""
    echo "🔧 To complete Facebook setup:"
    echo "1. Go to your Facebook App's Webhooks settings"
    echo "2. Add webhook URL: $FB_WEBHOOK_URL"
    echo "3. Use verify token: ${FB_VERIFY_TOKEN}"
    echo "4. Subscribe to 'messages' and 'messaging_postbacks' events"
    echo "5. Subscribe your webhook to your Facebook page"
fi

echo ""
echo "✅ Webhook setup complete!"
echo ""
echo "🧪 Test your bot:"
echo "  • Send a message to your Telegram bot"
echo "  • Send a message to your Facebook page"
echo ""
echo "📊 Check logs with: docker compose logs -f rasa"