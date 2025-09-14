# Rasa Multicanal (Telegram + Facebook) — Docker Ready

Bot con **Rasa 3.x** que expone webhooks para **Telegram** y **Facebook Messenger**, preparado para correr en **Docker** y trabajar desde **GitHub Codespaces** (ideal en iPad).

**✨ Características principales:**
- 🎠 **Carruseles interactivos** para Telegram y Facebook
- 🔄 **Workflows automatizados** con GitHub Actions
- 🐳 **Docker Ready** con docker-compose
- 🤖 **Actions personalizadas** para respuestas dinámicas
- 🔧 **CI/CD completo** con testing y deployment automático

---

## 🚀 Uso rápido

1. **Clona** este repo y crea tu `.env`:
   ```bash
   cp .env.example .env
   # Edita .env con tus tokens reales (NO lo subas al repo)
   ```

2. **Entrena el modelo** RASA:
   ```bash
   docker compose run --rm rasa rasa train
   ```

3. **Inicia los servicios**:
   ```bash
   docker compose up -d
   ```

4. **Prueba el bot** enviando mensajes como:
   - "hola" → Muestra saludo con botones interactivos
   - "servicios" → Despliega carrusel de servicios
   - "productos" → Muestra carrusel de planes
   - "ayuda" → Opciones de soporte

---

## 🎠 Carruseles Interactivos

Este bot incluye carruseles (carruelas) optimizados para cada plataforma:

### 📱 **Telegram**
- Teclados inline con botones personalizados
- URLs externas para más información
- Callback data para navegación interna
- Emojis y formato rich text

### 💬 **Facebook Messenger**
- Plantillas de carrusel nativas
- Imágenes y títulos atractivos
- Botones de acción (postback y web_url)
- Compatible con Generic Template

### 🔧 **Ejemplos de uso**

**Carrusel de Servicios:**
```
Usuario: "qué servicios ofrecen"
Bot: [Carrusel con 3 cards]
     📊 Consultoría Digital
     💻 Desarrollo Web  
     📱 Marketing Digital
```

**Carrusel de Productos:**
```
Usuario: "ver productos"
Bot: [Carrusel con planes]
     ⭐ Premium - $99/mes
     🔸 Standard - $49/mes
     📦 Básico - $19/mes
```

---

## ⚙️ CI/CD Workflows

El repositorio incluye 3 workflows automatizados:

### 🔍 **ci.yml** - Integración Continua
- ✅ Validación de archivos RASA
- 🧪 Testing de entrenamiento
- 🐳 Pruebas de Docker build
- 🔒 Escáner de seguridad

### 🚀 **deploy.yml** - Despliegue
- 📦 Build y push de imágenes Docker
- 🌍 Deploy a staging/producción
- 🔔 Notificaciones de estado

### 🐳 **docker-build.yml** - Construcción de Imágenes
- 🏗️ Multi-platform builds (AMD64/ARM64)
- 📋 Registro en GitHub Container Registry
- 🛡️ Análisis de vulnerabilidades

---

## 🗂️ Estructura del Proyecto

```
├── .github/workflows/     # GitHub Actions workflows
│   ├── ci.yml            # CI pipeline
│   ├── deploy.yml        # Deployment
│   └── docker-build.yml  # Docker builds
├── actions/              # Custom RASA actions
│   ├── __init__.py
│   ├── actions.py        # Carousel actions
│   └── test_actions.py   # Unit tests
├── data/                 # Training data
│   ├── nlu.yml          # Natural Language Understanding
│   ├── stories.yml      # Conversation flows
│   └── rules.yml        # Response rules
├── models/              # Trained models (generated)
├── config.yml           # RASA pipeline configuration
├── domain.yml           # Bot domain with carousel responses
├── credentials.yml      # Channel credentials
├── docker-compose.yml   # Multi-service setup
└── Dockerfile          # Custom actions container
```
