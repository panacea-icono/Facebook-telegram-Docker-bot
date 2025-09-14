#!/bin/bash

# Setup script para el bot Facebook-Telegram
echo "🤖 Configurando bot Facebook-Telegram..."

# Crear archivo .env si no existe
if [ ! -f .env ]; then
    echo "📝 Creando archivo .env desde .env.example..."
    cp .env.example .env
    echo "⚠️  IMPORTANTE: Edita el archivo .env con tus tokens reales antes de continuar"
    echo "   - TELEGRAM_BOT_TOKEN: Token de tu bot de Telegram"
    echo "   - FB_PAGE_TOKEN: Token de acceso de tu página de Facebook"
    echo "   - FB_APP_SECRET: Secret de tu aplicación de Facebook"
    echo "   - FB_VERIFY_TOKEN: Token de verificación personalizado"
else
    echo "✅ Archivo .env ya existe"
fi

# Verificar Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker no está instalado. Instala Docker primero."
    exit 1
fi

echo "🐳 Construyendo imágenes Docker..."
docker compose build

echo "✅ Setup completado!"
echo ""
echo "Para iniciar el bot:"
echo "  docker compose up"
echo ""
echo "Para iniciar en modo detached:"
echo "  docker compose up -d"
echo ""
echo "Para ver logs:"
echo "  docker compose logs -f"