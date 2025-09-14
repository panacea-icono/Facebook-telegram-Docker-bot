"""
Facebook Messenger Bot - Flask Application
Bot modular para gestión de redes sociales con Facebook Messenger
Desarrollado por Panacea Icono S.A.
"""

from flask import Flask, request, jsonify
import os
import requests
import logging
from datetime import datetime
from typing import Dict, Any, Optional

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Variables de entorno
VERIFY_TOKEN = os.getenv("FB_VERIFY_TOKEN", "change-me")
PAGE_TOKEN = os.getenv("FB_PAGE_TOKEN", "")
FB_API_VERSION = os.getenv("FB_API_VERSION", "v20.0")
PORT = int(os.getenv("PORT", "8080"))

class FacebookMessengerBot:
    """Clase principal para manejo del bot de Facebook Messenger"""
    
    def __init__(self, page_token: str, api_version: str = "v20.0"):
        self.page_token = page_token
        self.api_version = api_version
        self.base_url = f"https://graph.facebook.com/{api_version}/me/messages"
    
    def send_text_message(self, psid: str, text: str) -> Dict[str, Any]:
        """
        Envía un mensaje de texto al usuario
        
        Args:
            psid: ID del usuario en Facebook
            text: Texto del mensaje
            
        Returns:
            Respuesta de la API de Facebook
        """
        try:
            url = self.base_url
            params = {"access_token": self.page_token}
            payload = {
                "recipient": {"id": psid},
                "message": {"text": text}
            }
            
            response = requests.post(url, params=params, json=payload, timeout=10)
            response.raise_for_status()
            
            logger.info(f"Mensaje enviado exitosamente a {psid}")
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error enviando mensaje a {psid}: {e}")
            raise
    
    def send_quick_reply(self, psid: str, text: str, quick_replies: list) -> Dict[str, Any]:
        """
        Envía un mensaje con botones de respuesta rápida
        
        Args:
            psid: ID del usuario en Facebook
            text: Texto del mensaje
            quick_replies: Lista de botones de respuesta rápida
            
        Returns:
            Respuesta de la API de Facebook
        """
        try:
            url = self.base_url
            params = {"access_token": self.page_token}
            payload = {
                "recipient": {"id": psid},
                "message": {
                    "text": text,
                    "quick_replies": quick_replies
                }
            }
            
            response = requests.post(url, params=params, json=payload, timeout=10)
            response.raise_for_status()
            
            logger.info(f"Quick reply enviado exitosamente a {psid}")
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error enviando quick reply a {psid}: {e}")
            raise
    
    def send_template_message(self, psid: str, template: Dict[str, Any]) -> Dict[str, Any]:
        """
        Envía un mensaje con template (botones, tarjetas, etc.)
        
        Args:
            psid: ID del usuario en Facebook
            template: Template del mensaje
            
        Returns:
            Respuesta de la API de Facebook
        """
        try:
            url = self.base_url
            params = {"access_token": self.page_token}
            payload = {
                "recipient": {"id": psid},
                "message": {"attachment": template}
            }
            
            response = requests.post(url, params=params, json=payload, timeout=10)
            response.raise_for_status()
            
            logger.info(f"Template enviado exitosamente a {psid}")
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error enviando template a {psid}: {e}")
            raise

# Inicializar bot
bot = FacebookMessengerBot(PAGE_TOKEN, FB_API_VERSION)

def process_text_message(psid: str, text: str) -> str:
    """
    Procesa mensajes de texto y genera respuestas inteligentes
    
    Args:
        psid: ID del usuario
        text: Texto del mensaje
        
    Returns:
        Respuesta generada
    """
    text_lower = text.lower().strip()
    
    # Comandos básicos
    if text_lower in ['hola', 'hi', 'hello', 'buenos días', 'buenas tardes', 'buenas noches']:
        return "👋 ¡Hola! Soy el bot de Panacea Icono. ¿En qué puedo ayudarte hoy?"
    
    elif text_lower in ['ayuda', 'help', 'comandos']:
        return "🤖 Comandos disponibles:\n• 'info' - Información sobre Panacea Icono\n• 'servicios' - Nuestros servicios\n• 'contacto' - Información de contacto\n• 'menu' - Ver menú principal"
    
    elif text_lower in ['info', 'información']:
        return "🏥 **Panacea Icono S.A.**\n\nSomos una empresa especializada en soluciones tecnológicas para el sector salud, con enfoque en blockchain y Web3.\n\nNuestros productos incluyen PanasToken, PanasPay y PanasShop."
    
    elif text_lower in ['servicios', 'servicio']:
        return "💼 **Nuestros Servicios:**\n\n• **PanasToken**: Token ASA de Algorand para el ecosistema médico\n• **PanasPay**: Sistema de pagos P2P sin custodia\n• **PanasShop**: Marketplace con pagos Web3\n• **Desarrollo Blockchain**: Soluciones personalizadas"
    
    elif text_lower in ['contacto', 'contact']:
        return "📞 **Información de Contacto:**\n\n• Email: info@panacea-icono.com\n• Web: https://panacea-icono.com\n• GitHub: @panacea-icono\n\n¿Te gustaría recibir más información sobre algún servicio específico?"
    
    elif text_lower in ['menu', 'menú']:
        return "📋 **Menú Principal**\n\nSelecciona una opción:"
    
    else:
        return f"🤔 Entiendo que dices: '{text}'\n\nEscribe 'ayuda' para ver los comandos disponibles o 'menu' para ver las opciones principales."

def create_welcome_quick_replies() -> list:
    """Crea botones de respuesta rápida para el menú principal"""
    return [
        {
            "content_type": "text",
            "title": "ℹ️ Información",
            "payload": "INFO"
        },
        {
            "content_type": "text", 
            "title": "💼 Servicios",
            "payload": "SERVICIOS"
        },
        {
            "content_type": "text",
            "title": "📞 Contacto",
            "payload": "CONTACTO"
        },
        {
            "content_type": "text",
            "title": "🤖 Ayuda",
            "payload": "AYUDA"
        }
    ]

@app.route("/webhook", methods=["GET"])
def verify_webhook():
    """
    Verifica el webhook de Facebook Messenger
    """
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    
    logger.info(f"Verificación webhook - Mode: {mode}, Token: {token}")
    
    if mode == "subscribe" and token == VERIFY_TOKEN:
        logger.info("Webhook verificado exitosamente")
        return challenge, 200
    
    logger.warning("Verificación de webhook fallida")
    return "Forbidden", 403

@app.route("/webhook", methods=["POST"])
def receive_message():
    """
    Procesa mensajes recibidos del webhook de Facebook
    """
    try:
        data = request.get_json(force=True, silent=True) or {}
        logger.info(f"Mensaje recibido: {data}")
        
        for entry in data.get("entry", []):
            for event in entry.get("messaging", []):
                sender_id = event.get("sender", {}).get("id")
                
                if not sender_id:
                    continue
                
                # Procesar mensaje de texto
                if "message" in event and "text" in event["message"]:
                    text = event["message"]["text"].strip()
                    logger.info(f"Mensaje de texto de {sender_id}: {text}")
                    
                    # Generar respuesta
                    response_text = process_text_message(sender_id, text)
                    
                    # Enviar respuesta con botones si es el menú
                    if text.lower() in ['menu', 'menú']:
                        try:
                            bot.send_quick_reply(sender_id, response_text, create_welcome_quick_replies())
                        except Exception as e:
                            logger.error(f"Error enviando quick reply: {e}")
                            bot.send_text_message(sender_id, response_text)
                    else:
                        try:
                            bot.send_text_message(sender_id, response_text)
                        except Exception as e:
                            logger.error(f"Error enviando mensaje: {e}")
                
                # Procesar postbacks (botones)
                elif "postback" in event:
                    payload = event["postback"].get("payload", "")
                    logger.info(f"Postback de {sender_id}: {payload}")
                    
                    response_text = f"Recibí tu acción: {payload}"
                    
                    # Procesar postbacks específicos
                    if payload == "INFO":
                        response_text = "🏥 **Panacea Icono S.A.**\n\nSomos una empresa especializada en soluciones tecnológicas para el sector salud, con enfoque en blockchain y Web3."
                    elif payload == "SERVICIOS":
                        response_text = "💼 **Nuestros Servicios:**\n\n• **PanasToken**: Token ASA de Algorand\n• **PanasPay**: Pagos P2P sin custodia\n• **PanasShop**: Marketplace Web3\n• **Desarrollo Blockchain**: Soluciones personalizadas"
                    elif payload == "CONTACTO":
                        response_text = "📞 **Contacto:**\n\n• Email: info@panacea-icono.com\n• Web: https://panacea-icono.com\n• GitHub: @panacea-icono"
                    elif payload == "AYUDA":
                        response_text = "🤖 **Comandos disponibles:**\n\n• 'info' - Información\n• 'servicios' - Servicios\n• 'contacto' - Contacto\n• 'menu' - Menú principal"
                    
                    try:
                        bot.send_text_message(sender_id, response_text)
                    except Exception as e:
                        logger.error(f"Error enviando respuesta a postback: {e}")
                
                # Procesar otros tipos de mensajes
                elif "message" in event:
                    logger.info(f"Tipo de mensaje no procesado de {sender_id}: {event['message']}")
                    try:
                        bot.send_text_message(sender_id, "🤔 No puedo procesar este tipo de mensaje. Envía un texto o usa los botones disponibles.")
                    except Exception as e:
                        logger.error(f"Error enviando mensaje de error: {e}")
        
        return jsonify(success=True), 200
        
    except Exception as e:
        logger.error(f"Error procesando mensaje: {e}")
        return jsonify(success=False, error=str(e)), 500

@app.route("/health", methods=["GET"])
def health_check():
    """
    Endpoint de salud para monitoreo
    """
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "facebook-messenger-bot"
    }), 200

@app.route("/", methods=["GET"])
def home():
    """
    Página de inicio del bot
    """
    return jsonify({
        "message": "Facebook Messenger Bot - Panacea Icono S.A.",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "webhook": "/webhook",
            "health": "/health"
        }
    }), 200

if __name__ == "__main__":
    logger.info(f"Iniciando Facebook Messenger Bot en puerto {PORT}")
    logger.info(f"Token de verificación: {VERIFY_TOKEN[:10]}...")
    logger.info(f"Token de página: {'Configurado' if PAGE_TOKEN else 'NO CONFIGURADO'}")
    
    app.run(host="0.0.0.0", port=PORT, debug=False)
