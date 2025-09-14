"""
Webhook Handler
Maneja webhooks entrantes y salientes.
"""

from typing import Dict, Any
import json
import logging

logger = logging.getLogger(__name__)


class WebhookHandler:
    """Manejador de webhooks para diferentes plataformas."""
    
    def __init__(self):
        self.handlers = {
            'telegram': self._handle_telegram_webhook,
            'facebook': self._handle_facebook_webhook,
            'custom': self._handle_custom_webhook
        }
    
    def process_webhook(self, platform: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Procesa webhook según la plataforma."""
        try:
            handler = self.handlers.get(platform, self._handle_unknown_webhook)
            return handler(data)
        except Exception as e:
            logger.error(f"Error processing webhook for {platform}: {e}")
            return {"error": str(e), "status": "failed"}
    
    def _handle_telegram_webhook(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Maneja webhooks específicos de Telegram."""
        try:
            # Procesar datos específicos de Telegram
            message = data.get('message', {})
            chat_id = message.get('chat', {}).get('id')
            text = message.get('text', '')
            
            return {
                "platform": "telegram",
                "chat_id": chat_id,
                "message": text,
                "status": "processed"
            }
        except Exception as e:
            return {"error": str(e), "platform": "telegram"}
    
    def _handle_facebook_webhook(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Maneja webhooks específicos de Facebook."""
        try:
            # Procesar datos específicos de Facebook
            entry = data.get('entry', [{}])[0]
            messaging = entry.get('messaging', [{}])[0]
            sender_id = messaging.get('sender', {}).get('id')
            message = messaging.get('message', {}).get('text', '')
            
            return {
                "platform": "facebook",
                "sender_id": sender_id,
                "message": message,
                "status": "processed"
            }
        except Exception as e:
            return {"error": str(e), "platform": "facebook"}
    
    def _handle_custom_webhook(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Maneja webhooks personalizados."""
        return {
            "platform": "custom",
            "data": data,
            "status": "processed"
        }
    
    def _handle_unknown_webhook(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Maneja webhooks de plataformas desconocidas."""
        return {
            "platform": "unknown",
            "data": data,
            "status": "unhandled"
        }
    
    def send_webhook(self, url: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Envía webhook a URL externa."""
        try:
            import requests
            response = requests.post(url, json=data)
            return {
                "url": url,
                "status_code": response.status_code,
                "response": response.text,
                "status": "sent"
            }
        except Exception as e:
            return {"error": str(e), "status": "failed"}