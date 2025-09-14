# 🤖 Facebook Messenger Bot - Panacea Icono S.A.

Bot modular para gestión de redes sociales con **Facebook Messenger**, desarrollado con **Flask** y **Docker** para **Panacea Icono S.A.**

[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Facebook](https://img.shields.io/badge/Facebook-Messenger-0084FF?style=for-the-badge&logo=facebook&logoColor=white)](https://developers.facebook.com/)

## 🚀 Características

- ✅ **Webhook completo** para Facebook Messenger
- ✅ **Respuestas inteligentes** con procesamiento de texto
- ✅ **Botones interactivos** (Quick Replies)
- ✅ **Arquitectura modular** y escalable
- ✅ **Docker Ready** para producción
- ✅ **Logging estructurado** para monitoreo
- ✅ **Health checks** integrados
- ✅ **Seguridad** con usuario no-root
- ✅ **Configuración flexible** con variables de entorno

## 📋 Requisitos Previos

- **Docker** y **Docker Compose**
- **Cuenta de Facebook Developer**
- **Página de Facebook** para el bot
- **ngrok** o túnel público (para desarrollo)

## 🛠️ Instalación Rápida

### 1. Clonar y Configurar

```bash
# Clonar el repositorio
git clone https://github.com/panacea-icono/Facebook-telegram-Docker-bot.git
cd Facebook-telegram-Docker-bot

# Crear archivo de configuración
cp env.example .env

# Editar configuración
nano .env
```

### 2. Configurar Variables de Entorno

Edita el archivo `.env` con tus tokens:

```env
# Token de verificación (debe coincidir con Facebook)
FB_VERIFY_TOKEN=tu_token_unico_aqui

# Page Access Token de tu página
FB_PAGE_TOKEN=EAAG...tu_page_access_token

# Puerto del servidor
PORT=8080
```

### 3. Ejecutar con Docker

```bash
# Construir y ejecutar
docker-compose up --build

# O en modo desarrollo con hot-reload
docker-compose --profile dev up --build
```

El bot estará disponible en `http://localhost:8080`

## 🔧 Configuración en Facebook

### 1. Crear App de Facebook

1. Ve a [Facebook Developers](https://developers.facebook.com/)
2. Crea una nueva **App** → **Business** → **Messenger**
3. Agrega el producto **Messenger**

### 2. Configurar Webhook

1. En **Messenger** → **Settings** → **Webhooks**
2. **Callback URL**: `https://tu-dominio.com/webhook`
3. **Verify Token**: El mismo que configuraste en `FB_VERIFY_TOKEN`
4. **Suscribir campos**:
   - `messages`
   - `message_deliveries`
   - `messaging_postbacks`
   - `messaging_optins`

### 3. Generar Page Access Token

1. En **Messenger** → **Settings** → **Access Tokens**
2. Selecciona tu página
3. Genera el **Page Access Token**
4. Copia el token a `FB_PAGE_TOKEN` en tu `.env`

### 4. Suscribir Página

1. En **Messenger** → **Settings** → **Access Tokens**
2. Haz clic en **Subscribe** en tu página
3. Confirma la suscripción

## 🌐 Despliegue Público

### Opción 1: ngrok (Desarrollo)

```bash
# Instalar ngrok
npm install -g ngrok

# Crear túnel
ngrok http 8080

# Usar la URL HTTPS generada en Facebook
```

### Opción 2: Heroku (Producción)

```bash
# Instalar Heroku CLI
# Crear app
heroku create tu-bot-facebook

# Configurar variables
heroku config:set FB_VERIFY_TOKEN=tu_token
heroku config:set FB_PAGE_TOKEN=tu_page_token

# Desplegar
git push heroku main
```

### Opción 3: VPS con Docker

```bash
# En tu servidor
git clone https://github.com/panacea-icono/Facebook-telegram-Docker-bot.git
cd Facebook-telegram-Docker-bot
cp env.example .env
# Editar .env con tus tokens
docker-compose up -d
```

## 📱 Uso del Bot

### Comandos Disponibles

- `hola` - Saludo inicial
- `ayuda` - Ver comandos disponibles
- `info` - Información sobre Panacea Icono
- `servicios` - Nuestros servicios
- `contacto` - Información de contacto
- `menu` - Menú principal con botones

### Respuestas Inteligentes

El bot procesa mensajes de texto y responde de manera contextual:

- **Saludos**: Respuesta amigable
- **Comandos**: Información específica
- **Preguntas**: Respuestas contextuales
- **Botones**: Interacción con Quick Replies

## 🏗️ Arquitectura

```
facebook-bot/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias Python
├── Dockerfile            # Imagen Docker
├── docker-compose.yml    # Orquestación de contenedores
├── env.example          # Variables de entorno
└── README.md            # Documentación
```

### Estructura del Código

- **`FacebookMessengerBot`**: Clase principal para manejo de mensajes
- **`process_text_message()`**: Procesamiento inteligente de texto
- **`verify_webhook()`**: Verificación de webhook
- **`receive_message()`**: Procesamiento de mensajes entrantes

## 🔒 Seguridad

- ✅ Usuario no-root en Docker
- ✅ Variables de entorno para secretos
- ✅ Validación de tokens
- ✅ Manejo seguro de errores
- ✅ Logging sin información sensible

## 📊 Monitoreo

### Health Check

```bash
# Verificar estado del bot
curl http://localhost:8080/health
```

### Logs

```bash
# Ver logs del contenedor
docker-compose logs -f facebook-bot
```

## 🚀 Funcionalidades Avanzadas

### Quick Replies

El bot incluye botones interactivos para:
- Información de la empresa
- Servicios disponibles
- Información de contacto
- Ayuda y comandos

### Procesamiento Inteligente

- Reconocimiento de saludos
- Comandos contextuales
- Respuestas personalizadas
- Manejo de errores

## 🛠️ Desarrollo

### Estructura Modular

```python
# Agregar nuevos comandos
def process_text_message(psid: str, text: str) -> str:
    text_lower = text.lower().strip()
    
    if text_lower == 'nuevo_comando':
        return "Respuesta personalizada"
    
    # ... resto del código
```

### Agregar Nuevas Funcionalidades

1. **Nuevos tipos de mensaje**: Extender `receive_message()`
2. **Templates personalizados**: Usar `send_template_message()`
3. **Integración con APIs**: Agregar en `process_text_message()`

## 📈 Escalabilidad

- **Múltiples workers** con Gunicorn
- **Health checks** automáticos
- **Restart policies** en Docker
- **Logging estructurado** para análisis

## 🤝 Contribución

1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Desarrollado por **Panacea Icono S.A.** - Todos los derechos reservados.

## 📞 Soporte

- **Email**: info@panacea-icono.com
- **GitHub**: [@panacea-icono](https://github.com/panacea-icono)
- **Web**: [panacea-icono.com](https://panacea-icono.com)

---

**¡Listo para usar!** 🚀

Este bot está diseñado para ser el punto de entrada de **Panacea Icono S.A.** en las redes sociales, proporcionando información sobre nuestros servicios de blockchain y Web3 de manera interactiva y profesional.
