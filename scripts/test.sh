#!/bin/bash
# Run tests for Rasa model

set -euo pipefail

echo "🧪 Running Rasa model tests..."

# Check if model exists
if [ ! -d "models" ] || [ -z "$(ls -A models 2>/dev/null)" ]; then
    echo "⚠️  No trained model found. Please run ./scripts/train.sh first."
    exit 1
fi

echo "🔍 Running NLU tests..."
docker compose run --rm -T rasa test nlu --model models

echo ""
echo "📖 Running story tests..."
docker compose run --rm -T rasa test core --model models

echo ""
echo "🎯 Running end-to-end tests..."
docker compose run --rm -T rasa test --model models

echo ""
echo "📊 Generating test results..."
docker compose run --rm -T rasa test --model models --out results

echo "✅ Tests completed! Check the results/ directory for detailed reports."

# Optional: Open results if available
if command -v xdg-open &> /dev/null; then
    echo "📈 Opening test results..."
    xdg-open results/intent_report.html 2>/dev/null || echo "HTML report available at: results/intent_report.html"
fi