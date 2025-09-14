# Rasa Multicanal (Telegram + Facebook) — Docker Ready

Bot inteligente construido con Rasa 3.x que funciona simultáneamente en Telegram y Facebook Messenger, completamente contenerizado con Docker y listo para ejecutar en GitHub Codespaces.

## 🚀 Características

- **Multicanal**: Funciona en Telegram y Facebook Messenger
- **Rasa 3.x**: Última versión estable con arquitectura moderna
- **Docker Ready**: Levanta con un comando usando Docker Compose
- **GitHub Codespaces**: Compatible con desarrollo en iPad/tablet
- **Webhooks Expuestos**: Endpoints listos para configuración
- **Seguridad**: Manejo de secretos via variables de entorno

## 📁 Estructura del Proyecto

```
.
├── README.md                 # Este archivo
├── docker-compose.yml        # Configuración de servicios Docker
├── config.yml               # Configuración del pipeline Rasa
├── credentials.yml          # Credenciales de canales (con variables de entorno)
├── endpoints.yml            # Endpoints de actions
├── domain.yml               # Definición de dominio (intents, actions, responses)
├── .env.example             # Template de variables de entorno
├── data/
│   ├── nlu.yml              # Datos de entrenamiento NLU
│   └── stories.yml          # Historias de conversación
└── actions/
    ├── __init__.py
    └── actions.py           # Acciones personalizadas
```

## 🛠️ Configuración Inicial

### 1. Configurar Variables de Entorno

Copia el archivo de ejemplo y configura tus tokens:

```bash
cp .env.example .env
```

Edita `.env` con tus credenciales reales:

```env
TELEGRAM_BOT_TOKEN=tu_token_real_de_telegram
FB_PAGE_TOKEN=tu_token_de_pagina_facebook
FB_APP_SECRET=tu_app_secret_de_facebook
FB_VERIFY_TOKEN=tu_palabra_secreta_personalizada
RASA_PRO_TOKEN=opcional_token_rasa_pro
```

### 2. Obtener Credenciales

#### Telegram Bot Token
1. Habla con [@BotFather](https://t.me/botfather) en Telegram
2. Crea un nuevo bot: `/newbot`
3. Sigue las instrucciones y guarda el token

#### Facebook Messenger
1. Ve a [Facebook for Developers](https://developers.facebook.com/)
2. Crea una nueva app
3. Agrega "Messenger" como producto
4. Obtén Page Access Token y App Secret
5. Define tu VERIFY_TOKEN personalizado

### 3. Entrenar el Modelo

```bash
docker compose run --rm rasa rasa train
```

### 4. Levantar los Servicios

```bash
docker compose up
```

El bot estará disponible en:
- **API Rasa**: http://localhost:5005
- **Actions Server**: http://localhost:5055

## 🔗 Configuración de Webhooks

### Telegram

Configura el webhook ejecutando (reemplaza `<TOKEN>` y `<HOST>`):

```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://<HOST>/webhooks/telegram/webhook"
```

**Ejemplo con tu dominio**:
```bash
curl -X POST "https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/setWebhook?url=https://tudominio.com/webhooks/telegram/webhook"
```

### Facebook Messenger

1. Ve a la configuración de Webhooks en Facebook for Developers
2. Configura:
   - **Callback URL**: `https://<HOST>/webhooks/facebook/webhook`
   - **Verify Token**: El valor de `FB_VERIFY_TOKEN` de tu `.env`
3. Suscríbete a eventos: `messages`, `messaging_postbacks`

## 🧪 Probar el Bot

1. **En Telegram**: Busca tu bot y envía "hola"
2. **En Facebook Messenger**: Ve a tu página y envía "hola"

**Respuesta esperada**: "¡Hola! ¿En qué te ayudo?" seguido de "¡Hola, DR-TAPIA! Soy tu bot multicanal Rasa 🤖"

## 💻 GitHub Codespaces (iPad/Tablet Friendly)

### Configuración para Codespaces

1. **Fork este repositorio** en tu cuenta de GitHub
2. **Abre en Codespaces**: Click en "Code" → "Codespaces" → "Create codespace"
3. **Espera** que termine la configuración automática
4. **Configura variables**: Crea tu `.env` desde `.env.example`
5. **Entrena**: `docker compose run --rm rasa rasa train`
6. **Levanta**: `docker compose up`

### Acceso desde iPad/Tablet

1. **Instala GitHub Mobile** o usa el navegador
2. **Ve a tu repositorio** → "Code" → "Codespaces"
3. **Abre tu codespace** existente
4. **USA VS Code Web** para editar código
5. **Terminal integrada** para comandos Docker

### Port Forwarding en Codespaces

Codespaces automáticamente hace forwarding de los puertos:
- Puerto 5005 (Rasa) será accesible como `https://<codespace-name>-5005.githubpreview.dev`
- Usa esta URL para configurar tus webhooks

## 🔍 Debugging y Logs

### Ver logs en tiempo real

```bash
# Logs de todos los servicios
docker compose logs -f

# Solo logs de Rasa
docker compose logs -f rasa

# Solo logs de Actions
docker compose logs -f actions
```

### Comandos útiles de debugging

```bash
# Validar configuración
docker compose run --rm rasa rasa data validate

# Modo interactivo para testing
docker compose run --rm rasa rasa shell

# Reiniciar servicios
docker compose restart

# Reconstruir imágenes
docker compose build --no-cache
```

### Troubleshooting Común

**Error: "No module named 'actions'"**
- Verifica que el volumen `./actions:/app/actions` esté correctamente montado

**Error: "Connection refused to actions server"**
- Asegúrate que ambos servicios estén en la misma red (`rasa-network`)

**Webhook no recibe mensajes**
- Verifica que tu dominio tenga HTTPS habilitado
- Confirma que los tokens sean correctos
- Revisa logs: `docker compose logs -f rasa`

## 🌐 Despliegue en Producción

### Render / Railway

1. **Conecta tu repositorio** GitHub
2. **Configura variables de entorno** en el panel:
   ```
   TELEGRAM_BOT_TOKEN=tu_token
   FB_PAGE_TOKEN=tu_token
   FB_APP_SECRET=tu_secret
   FB_VERIFY_TOKEN=tu_verify_token
   ```
3. **Dockerfile** (si necesitas uno personalizado):
   ```dockerfile
   FROM rasa/rasa:3.6.18-full
   COPY . /app
   WORKDIR /app
   RUN rasa train
   CMD ["run", "--enable-api", "--cors", "*", "--port", "5005"]
   ```

### Cloudflare Proxy + Dominios

1. **Configura tu dominio** en Cloudflare
2. **Habilita Proxy** (nube naranja) para HTTPS automático
3. **Actualiza webhooks** con tu dominio personalizado:
   - `https://tubot.tudominio.com/webhooks/telegram/webhook`
   - `https://tubot.tudominio.com/webhooks/facebook/webhook`

## 🛡️ Seguridad

### ⚠️ IMPORTANTE: Manejo de Secretos

- **NUNCA** commitees el archivo `.env` real
- **USA GitHub Secrets** para despliegues automatizados
- **ROTA tokens** periódicamente
- **VERIFICA** que `.env` esté en `.gitignore`

### GitHub Secrets para CI/CD

En tu repositorio GitHub: Settings → Secrets and variables → Actions

Agrega estos secrets:
- `TELEGRAM_BOT_TOKEN`
- `FB_PAGE_TOKEN`
- `FB_APP_SECRET`
- `FB_VERIFY_TOKEN`

## 📝 Contribución

### Checklist de Conexión Telegram/Facebook

Antes de reportar problemas, verifica:

- [ ] `.env` configurado con tokens correctos
- [ ] `docker compose up` funciona sin errores
- [ ] Puerto 5005 accesible (http://localhost:5005)
- [ ] Modelo entrenado (`docker compose run --rm rasa rasa train`)
- [ ] Webhook configurado con HTTPS
- [ ] Tokens válidos y no expirados
- [ ] Logs no muestran errores (`docker compose logs -f`)

### Reportar Issues

**Para bugs**, incluye:
- Logs completos: `docker compose logs`
- Tu configuración (sin secretos)
- Pasos para reproducir

**Para nuevas funcionalidades**:
- Describe el caso de uso
- Propón la implementación
- Considera la compatibilidad multicanal

## 🏆 Funcionalidades Actuales

- ✅ **Intent "saludo"**: Reconoce múltiples formas de saludar
- ✅ **Acción personalizada**: Respuesta específica a DR-TAPIA
- ✅ **Multicanal**: Funciona en Telegram y Facebook
- ✅ **Docker**: Completamente contenerizado
- ✅ **Variables de entorno**: Configuración segura

## 🎯 Roadmap

- [ ] Más intents (despedida, preguntas frecuentes)
- [ ] Integración con WhatsApp Business
- [ ] Dashboard de métricas
- [ ] Soporte para archivos multimedia
- [ ] Integración con bases de datos
- [ ] Tests automatizados

---

**¡Hecho con ❤️ para DR-TAPIA!** 🤖

Para soporte o preguntas, abre un issue en este repositorio.
