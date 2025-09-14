#!/bin/bash
# Clean up Rasa project resources

set -euo pipefail

echo "🧹 Cleaning up Rasa project resources..."

# Stop services first
echo "🛑 Stopping services..."
docker compose down

# Remove containers, networks, volumes, and images created by up
echo "🗑️  Removing containers, networks, and volumes..."
docker compose down --volumes --remove-orphans

# Clean up Docker images related to the project
echo "🖼️  Cleaning up project Docker images..."
docker compose down --rmi all --volumes --remove-orphans

# Remove generated models (optional)
if [ -t 0 ]; then
    read -p "🤖 Remove trained models? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🗑️  Removing models directory..."
        rm -rf models/
    fi
else
    echo "ℹ️  Skipping model removal (non-interactive mode)"
fi

# Remove test results (optional)
if [ -t 0 ]; then
    read -p "📊 Remove test results? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🗑️  Removing results directory..."
        rm -rf results/
    fi
else
    echo "ℹ️  Skipping test results removal (non-interactive mode)"
fi

# Remove logs (optional)
if [ -t 0 ]; then
    read -p "📝 Remove log files? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🗑️  Removing log files..."
        rm -rf logs/
        rm -f rasa.log
        rm -f *.log
    fi
else
    echo "ℹ️  Skipping log files removal (non-interactive mode)"
fi

# Clean up Docker system (optional)
if [ -t 0 ]; then
    read -p "🐳 Run Docker system prune? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🧹 Running Docker system prune..."
        docker system prune -f
    fi
else
    echo "ℹ️  Skipping Docker system prune (non-interactive mode)"
fi

echo ""
echo "✅ Cleanup complete!"
echo ""
echo "To start fresh:"
echo "1. Run: ./scripts/train.sh"
echo "2. Run: ./scripts/up.sh"