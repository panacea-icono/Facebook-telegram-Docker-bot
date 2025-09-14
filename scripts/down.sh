#!/bin/bash
# Stop Rasa services using Docker Compose

set -euo pipefail

echo "🛑 Stopping Rasa multicanal bot services..."

# Stop and remove containers
docker compose down

echo "✅ Services stopped successfully!"

# Optional: Show remaining containers
echo ""
echo "📊 Current running containers:"
docker ps --filter "name=facebook-telegram-docker-bot" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo ""
echo "To start services again, run: ./scripts/up.sh"