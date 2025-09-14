# Facebook-telegram-Docker-bot

Bot de gestión de redes sociales desarrollado con Rasa 3.x, soporta múltiples canales (Telegram y Facebook Messenger) y está completamente dockerizado.

## 🚀 Características

- **Rasa 3.x**: Framework conversacional de última generación
- **Multicanal**: Soporte para Telegram y Facebook Messenger
- **Docker**: Completamente containerizado para fácil despliegue
- **Redis**: Almacenamiento persistente de conversaciones
- **Variables de entorno**: Configuración segura sin credenciales hardcodeadas
- **Acción personalizada**: Responde "¡Hola, DR-TAPIA!" como acción mínima

## 📁 Estructura del proyecto

```
├── actions/
│   ├── __init__.py
│   └── actions.py          # Acciones personalizadas
├── data/
│   ├── nlu.yml            # Datos de entrenamiento NLU
│   └── stories.yml        # Historias de conversación
├── models/
│   └── .gitkeep
├── config.yml             # Configuración del pipeline Rasa
├── credentials.yml        # Credenciales de canales
├── domain.yml            # Dominio del bot
├── endpoints.yml         # Configuración de endpoints
├── docker-compose.yml    # Orquestación de servicios
├── Dockerfile            # Imagen Docker personalizada
├── .env.example          # Variables de entorno de ejemplo
└── requirements-actions.txt
```

## 🛠️ Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/panacea-icono/Facebook-telegram-Docker-bot.git
cd Facebook-telegram-Docker-bot
```

### 2. Configurar variables de entorno

```bash
cp .env.example .env
```

Edita el archivo `.env` con tus credenciales reales:

#### Para Telegram:
1. Crea un bot con [@BotFather](https://t.me/botfather)
2. Obtén el token del bot
3. Configura `TELEGRAM_ACCESS_TOKEN`

#### Para Facebook Messenger:
1. Crea una aplicación en [Facebook Developers](https://developers.facebook.com/)
2. Configura Messenger como producto
3. Obtén `FACEBOOK_PAGE_ACCESS_TOKEN` y `FACEBOOK_APP_SECRET`

### 3. Entrenar el modelo

```bash
docker-compose run --rm rasa train
```

### 4. Iniciar los servicios

```bash
docker-compose up -d
```

## 🔗 Configuración de Webhooks

### Telegram

1. Configura tu webhook URL:
```bash
curl -X POST \
  https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://tu-dominio.com/webhooks/telegram/webhook"
  }'
```

### Facebook Messenger

1. En la configuración de tu app de Facebook:
   - Webhooks URL: `https://tu-dominio.com/webhooks/facebook/webhook`
   - Verify Token: El valor de `FACEBOOK_VERIFY` en tu `.env`
   - Suscríbete a los eventos: `messages`, `messaging_postbacks`

## 🛡️ Seguridad

### Mejores prácticas implementadas:

1. **Variables de entorno**: Todas las credenciales se configuran mediante variables de entorno
2. **Tokens de verificación**: Webhooks protegidos con tokens de verificación
3. **Redis**: Almacenamiento seguro de sesiones
4. **Docker**: Aislamiento de la aplicación

### Recomendaciones adicionales:

1. **HTTPS obligatorio**: Usa siempre HTTPS para webhooks
2. **Firewall**: Limita el acceso a puertos específicos
3. **Rotación de tokens**: Cambia regularmente tus tokens de acceso
4. **Monitoreo**: Implementa logging y monitoreo de seguridad

```bash
# Generar un secret aleatorio para webhooks
openssl rand -hex 32
```

## 🚀 Comandos útiles

### Entrenar el modelo
```bash
docker-compose run --rm rasa train
```

### Ejecutar en modo desarrollo
```bash
docker-compose up
```

### Ver logs
```bash
docker-compose logs -f rasa
docker-compose logs -f action-server
```

### Acceder al shell de Rasa
```bash
docker-compose run --rm rasa shell
```

### Validar los datos de entrenamiento
```bash
docker-compose run --rm rasa data validate
```

### Probar el modelo
```bash
docker-compose run --rm rasa test
```

## 🔧 Personalización

### Agregar nuevos intents

1. Edita `data/nlu.yml` para agregar ejemplos de entrenamiento
2. Actualiza `domain.yml` con los nuevos intents
3. Modifica `data/stories.yml` para incluir nuevos flujos
4. Entrena el modelo: `docker-compose run --rm rasa train`

### Crear nuevas acciones personalizadas

1. Edita `actions/actions.py`
2. Agrega la acción al `domain.yml`
3. Reinicia el action server: `docker-compose restart action-server`

## 📚 Documentación adicional

- [Rasa Documentation](https://rasa.com/docs/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Facebook Messenger Platform](https://developers.facebook.com/docs/messenger-platform)

## 🐛 Solución de problemas

### El bot no responde
1. Verifica que los servicios estén ejecutándose: `docker-compose ps`
2. Revisa los logs: `docker-compose logs`
3. Confirma que las credenciales sean correctas

### Errores de webhook
1. Verifica que la URL sea accesible públicamente
2. Confirma que el certificado SSL sea válido
3. Revisa los tokens de verificación

### Problemas de entrenamiento
1. Valida los datos: `docker-compose run --rm rasa data validate`
2. Revisa la configuración en `config.yml`
3. Verifica que hay suficientes ejemplos de entrenamiento

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request
