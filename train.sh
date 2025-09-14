#!/bin/bash

# Script para entrenar el modelo de Rasa
echo "🧠 Entrenando modelo de Rasa..."

# Verificar si existe la configuración
if [ ! -f "config.yml" ] || [ ! -f "domain.yml" ]; then
    echo "❌ Faltan archivos de configuración (config.yml, domain.yml)"
    exit 1
fi

# Verificar si existen datos de entrenamiento
if [ ! -d "data" ]; then
    echo "❌ Directorio de datos no encontrado"
    exit 1
fi

# Crear directorio de modelos si no existe
mkdir -p models

echo "📚 Validando datos de entrenamiento..."
docker run --rm -v $(pwd):/app rasa/rasa:3.6.18-full validate --fail-on-warnings

echo "🚀 Entrenando modelo..."
docker run --rm -v $(pwd):/app rasa/rasa:3.6.18-full train

echo "✅ Entrenamiento completado!"
echo "📁 El modelo entrenado está en el directorio ./models/"

# Mostrar archivos de modelo generados
echo ""
echo "Modelos disponibles:"
ls -la models/