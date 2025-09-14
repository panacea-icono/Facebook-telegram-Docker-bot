#!/bin/bash

# Facebook Messenger Bot - Script de Configuración
# Desarrollado por Panacea Icono S.A.

set -e

echo "🤖 Configurando Facebook Messenger Bot - Panacea Icono S.A."
echo "=================================================="

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para imprimir mensajes con color
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Verificar si Docker está instalado
if ! command -v docker &> /dev/null; then
    print_error "Docker no está instalado. Por favor instala Docker primero."
    exit 1
fi

# Verificar si Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose no está instalado. Por favor instala Docker Compose primero."
    exit 1
fi

print_status "Docker y Docker Compose encontrados"

# Crear archivo .env si no existe
if [ ! -f .env ]; then
    print_info "Creando archivo .env desde env.example..."
    cp env.example .env
    print_warning "IMPORTANTE: Debes editar el archivo .env con tus tokens reales de Facebook"
    print_warning "Archivo .env creado. Edítalo antes de continuar."
    echo ""
    echo "Variables que debes configurar:"
    echo "- FB_VERIFY_TOKEN: Token de verificación del webhook"
    echo "- FB_PAGE_TOKEN: Page Access Token de tu página de Facebook"
    echo ""
    read -p "¿Has configurado el archivo .env? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_info "Configura el archivo .env y ejecuta este script nuevamente"
        exit 0
    fi
else
    print_status "Archivo .env ya existe"
fi

# Verificar que las variables estén configuradas
if grep -q "pon-un-token-unico-para-verificar" .env; then
    print_error "Debes configurar FB_VERIFY_TOKEN en el archivo .env"
    exit 1
fi

if grep -q "EAAG...tu_page_access_token_aqui" .env; then
    print_error "Debes configurar FB_PAGE_TOKEN en el archivo .env"
    exit 1
fi

print_status "Variables de entorno configuradas correctamente"

# Construir la imagen Docker
print_info "Construyendo imagen Docker..."
docker-compose build

if [ $? -eq 0 ]; then
    print_status "Imagen Docker construida exitosamente"
else
    print_error "Error construyendo la imagen Docker"
    exit 1
fi

# Verificar que el contenedor se puede ejecutar
print_info "Verificando que el bot funciona correctamente..."
docker-compose up -d

# Esperar un momento para que el contenedor se inicie
sleep 5

# Verificar health check
if curl -s http://localhost:8080/health > /dev/null; then
    print_status "Bot funcionando correctamente en http://localhost:8080"
else
    print_warning "El bot no responde en el puerto 8080. Verifica los logs:"
    echo "docker-compose logs facebook-bot"
fi

# Mostrar información de uso
echo ""
echo "🎉 ¡Configuración completada!"
echo "================================"
echo ""
echo "Comandos útiles:"
echo "• Ver logs: docker-compose logs -f facebook-bot"
echo "• Detener: docker-compose down"
echo "• Reiniciar: docker-compose restart"
echo "• Estado: docker-compose ps"
echo ""
echo "Endpoints disponibles:"
echo "• Webhook: http://localhost:8080/webhook"
echo "• Health: http://localhost:8080/health"
echo "• Home: http://localhost:8080/"
echo ""
echo "Para desarrollo con hot-reload:"
echo "• docker-compose --profile dev up"
echo ""
print_warning "Recuerda configurar el webhook en Facebook Developer Console"
print_warning "URL del webhook: https://tu-dominio.com/webhook"
print_warning "Token de verificación: El mismo que configuraste en FB_VERIFY_TOKEN"
