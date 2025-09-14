#!/bin/bash

# Script para probar el bot localmente
echo "🧪 Probando bot Facebook-Telegram..."

# Verificar si existe un modelo entrenado
if [ ! -d "models" ] || [ -z "$(ls -A models/)" ]; then
    echo "❌ No hay modelos entrenados. Ejecuta ./train.sh primero"
    exit 1
fi

# Verificar archivo .env
if [ ! -f ".env" ]; then
    echo "❌ Archivo .env no encontrado. Ejecuta ./setup.sh primero"
    exit 1
fi

echo "🚀 Iniciando servicios de prueba..."

# Iniciar solo el servidor de acciones para pruebas
echo "📡 Iniciando servidor de acciones..."
docker compose up actions -d

echo "⏳ Esperando que el servidor de acciones esté listo..."
sleep 10

# Verificar que el servidor de acciones esté funcionando
if curl -f http://localhost:5055/health > /dev/null 2>&1; then
    echo "✅ Servidor de acciones funcionando en http://localhost:5055"
else
    echo "❌ Servidor de acciones no responde"
    docker compose logs actions
    exit 1
fi

echo "🗣️  Iniciando shell interactiva de Rasa..."
echo "   Puedes probar el bot escribiendo mensajes"
echo "   Escribe 'quit' para salir"

docker run --rm -it --network host -v $(pwd):/app rasa/rasa:3.6.18-full shell --endpoints endpoints.yml

echo "🛑 Deteniendo servicios de prueba..."
docker compose down