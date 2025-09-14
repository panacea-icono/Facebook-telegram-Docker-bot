# 🤖 Rasa Multicanal (Telegram + Facebook) — Docker Ready

Bot con **Rasa 3.x** que expone webhooks para **Telegram** y **Facebook Messenger**, preparado para correr en **Docker** y trabajar desde **GitHub Codespaces** (ideal en iPad).

## 📋 Características

- ✅ **Multicanal**: Telegram y Facebook Messenger
- ✅ **Docker Ready**: Fácil despliegue con docker-compose
- ✅ **Acciones Personalizadas**: Detección automática de plataforma
- ✅ **Integraciones**: Pagos (Stripe, TON), APIs externas
- ✅ **Modular**: Estructura organizada y extensible
- ✅ **GitHub Codespaces**: Compatible para desarrollo en iPad/tablet

---

## 🚀 Inicio Rápido

### 1. **Configuración inicial**
```bash
# Clonar y configurar
git clone https://github.com/panacea-icono/Facebook-telegram-Docker-bot.git
cd Facebook-telegram-Docker-bot
./setup.sh
```

### 2. **Configurar tokens**
Edita el archivo `.env` con tus tokens reales:
```bash
# Telegram Bot Token (obtener de @BotFather)
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz

# Facebook Tokens (obtener desde Facebook for Developers)
FB_PAGE_TOKEN=tu_page_access_token
FB_APP_SECRET=tu_app_secret
FB_VERIFY_TOKEN=tu_verify_token_personalizado
```

### 3. **Entrenar modelo**
```bash
./train.sh
```

### 4. **Probar localmente**
```bash
./test.sh
```

### 5. **Iniciar en producción**
```bash
docker compose up -d
```

---

## 📁 Estructura del Proyecto

```
📦 Facebook-telegram-Docker-bot
├── 🐳 docker-compose.yml      # Configuración Docker
├── 🐳 Dockerfile             # Imagen para acciones
├── ⚙️  config.yml             # Configuración Rasa NLU/Core
├── 🎯 domain.yml             # Dominio del bot (intents, responses)
├── 📡 credentials.yml        # Credenciales de canales
├── 🔗 endpoints.yml          # Endpoints y conexiones
├── 📊 data/                  # Datos de entrenamiento
│   ├── nlu.yml              # Datos NLU (intents/examples)
│   ├── stories.yml          # Historias de conversación
│   └── rules.yml            # Reglas del bot
├── 🎬 actions/               # Acciones personalizadas
│   ├── __init__.py
│   └── actions.py           # Lógica de acciones
├── 🔌 integrations/          # Integraciones externas
│   ├── __init__.py
│   ├── payments.py          # Procesador de pagos
│   ├── webhooks.py          # Manejador de webhooks
│   └── external_apis.py     # Cliente APIs externas
├── 📋 requirements.txt       # Dependencias Python
├── 🔧 setup.sh              # Script de configuración
├── 🧠 train.sh              # Script de entrenamiento
├── 🧪 test.sh               # Script de pruebas
├── 📝 .env.example          # Plantilla de variables de entorno
└── 📖 README.md             # Esta documentación
```

---

## 🛠️ Desarrollo

### **Configuración para desarrollo**
```bash
# Crear archivo .env
cp .env.example .env

# Instalar dependencias localmente (opcional)
pip install -r requirements.txt

# Validar configuración
rasa data validate

# Entrenar modelo
rasa train

# Probar en shell interactiva
rasa shell
```

### **Añadir nuevas integraciones**
1. Crear nuevo archivo en `integrations/`
2. Añadir importación en `integrations/__init__.py`
3. Usar en `actions/actions.py`

### **Añadir nuevos canales**
1. Actualizar `credentials.yml`
2. Configurar variables en `.env.example`
3. Añadir lógica específica en acciones

---

## 🔌 Integraciones Disponibles

### **Pagos**
- **Stripe**: Procesamiento de pagos con tarjeta
- **TON**: Pagos con criptomonedas TON

### **APIs Externas**
- **Clima**: Información meteorológica
- **Noticias**: Últimas noticias por categoría
- **Notificaciones**: Sistema de notificaciones externas

### **Webhooks**
- **Telegram**: Webhooks nativos
- **Facebook**: Webhooks de Messenger
- **Personalizados**: Webhooks configurables

---

## 🚀 Despliegue

### **Docker (Recomendado)**
```bash
# Construcción y inicio
docker compose up --build -d

# Ver logs
docker compose logs -f

# Reiniciar servicios
docker compose restart

# Parar servicios
docker compose down
```

### **GitHub Codespaces**
1. Abrir repositorio en GitHub
2. Clic en "Code" → "Codespaces" → "Create codespace"
3. Ejecutar `./setup.sh` en la terminal
4. Configurar `.env` con tus tokens
5. Ejecutar `./train.sh` y luego `docker compose up`

### **Producción**
```bash
# Con variables de entorno
TELEGRAM_BOT_TOKEN=tu_token \
FB_PAGE_TOKEN=tu_token \
docker compose up -d

# O usando .env
docker compose --env-file .env.prod up -d
```

---

## 🔧 Comandos Útiles

```bash
# Validar datos de entrenamiento
rasa data validate

# Entrenar modelo específico
rasa train --config config.yml --domain domain.yml

# Evaluar modelo
rasa test

# Exportar conversaciones
rasa export

# Ver métricas del servidor
curl http://localhost:5005/status
curl http://localhost:5055/health
```

---

## 🐛 Solución de Problemas

### **Error: "No module named 'actions'"**
```bash
# Reconstruir imagen de acciones
docker compose build actions
docker compose restart actions
```

### **Error: "Model not found"**
```bash
# Entrenar nuevo modelo
./train.sh
docker compose restart rasa
```

### **Webhooks no funcionan**
1. Verificar tokens en `.env`
2. Confirmar URLs de webhook en plataformas
3. Revisar logs: `docker compose logs -f`

---

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo `LICENSE` para más detalles.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:
1. Fork del proyecto
2. Crear feature branch (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Añadir nueva funcionalidad'`)
4. Push branch (`git push origin feature/nueva-funcionalidad`)
5. Abrir Pull Request

---

## 📞 Soporte

- 📧 **Email**: soporte@ejemplo.com
- 💬 **Telegram**: [@soporte_bot]
- 🐙 **Issues**: [GitHub Issues](https://github.com/panacea-icono/Facebook-telegram-Docker-bot/issues)
