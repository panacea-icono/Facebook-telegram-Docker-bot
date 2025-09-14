## 🔗 Checklist de Conexión Telegram/Facebook

**Antes de reportar problemas, verifica que:**

### ✅ Configuración Básica
- [ ] Copiaste `.env.example` a `.env`
- [ ] Completaste todas las variables de entorno en `.env`
- [ ] Los tokens no tienen espacios adicionales
- [ ] Los tokens no están expirados

### ✅ Docker y Servicios
- [ ] `docker compose config` no muestra errores
- [ ] `docker compose run --rm rasa train` completa exitosamente
- [ ] `docker compose up` inicia sin errores críticos
- [ ] Puerto 5005 está disponible: `curl http://localhost:5005`

### ✅ Webhooks y Red
- [ ] Tu aplicación está disponible con HTTPS
- [ ] El dominio está configurado correctamente
- [ ] Los webhooks están configurados con las URLs correctas
- [ ] El certificado SSL es válido

### ✅ Telegram
- [ ] El bot fue creado con @BotFather
- [ ] El token comienza con un número seguido de ':'
- [ ] Webhook configurado: `https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://<HOST>/webhooks/telegram/webhook`
- [ ] Verificar webhook: `https://api.telegram.org/bot<TOKEN>/getWebhookInfo`

### ✅ Facebook Messenger
- [ ] La aplicación de Facebook está aprobada
- [ ] Los permisos de página están correctos
- [ ] Page Access Token es válido y no expirado
- [ ] App Secret coincide con la aplicación
- [ ] VERIFY_TOKEN coincide en la configuración de webhook y en `.env`

### 🐛 Debugging
- [ ] Revisé los logs: `docker compose logs -f`
- [ ] Los logs no muestran errores de conexión
- [ ] El modelo fue entrenado recientemente
- [ ] La acción personalizada `action_hola` está funcionando

### 📝 Para reportar un issue, incluye:
1. Logs completos: `docker compose logs`
2. Tu configuración (sin secretos)
3. Pasos exactos para reproducir el problema
4. Capturas de pantalla de errores (si aplica)

---
**💡 Tip**: Si todo está ✅ pero aún no funciona, intenta recrear los contenedores:
```bash
docker compose down
docker compose up --build
```