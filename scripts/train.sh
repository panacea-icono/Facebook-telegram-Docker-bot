#!/bin/bash
# Train Rasa model using Docker Compose

set -euo pipefail

echo "🚀 Training Rasa model..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found. Creating from .env.example..."
    cp .env.example .env
    echo "Please edit .env with your actual tokens before using the bot."
fi

# Train the model
docker compose run --rm -T rasa train

echo "✅ Training complete! Model saved to models/ directory."

# Optional: Test the model (only if running interactively)
if [ -t 0 ]; then
    read -p "Would you like to test the model? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🧪 Testing model..."
        docker compose run --rm -T rasa test
    fi
else
    echo "ℹ️  Run './scripts/test.sh' to test the trained model."
fi