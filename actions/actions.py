from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionDetectPlatform(Action):
    """Detecta la plataforma desde la que se está comunicando el usuario."""

    def name(self) -> Text:
        return "action_detect_platform"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Obtener metadatos del canal
        input_channel = tracker.get_latest_input_channel()
        
        platform = "unknown"
        if input_channel == "telegram":
            platform = "telegram"
        elif input_channel == "facebook":
            platform = "facebook"
        
        # Mensaje personalizado según la plataforma
        if platform == "telegram":
            dispatcher.utter_message(
                text="¡Hola! Veo que me escribes desde Telegram 📱"
            )
        elif platform == "facebook":
            dispatcher.utter_message(
                text="¡Hola! Veo que me escribes desde Facebook Messenger 💬"
            )
        else:
            dispatcher.utter_message(
                text="¡Hola! Te doy la bienvenida a nuestro bot multicanal"
            )

        return [SlotSet("platform", platform)]


class ActionCustomResponse(Action):
    """Respuesta personalizada con funcionalidades específicas por plataforma."""

    def name(self) -> Text:
        return "action_custom_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        platform = tracker.get_slot("platform")
        
        if platform == "telegram":
            # Funcionalidades específicas de Telegram
            dispatcher.utter_message(
                text="En Telegram puedes usar comandos como /start, /help",
                buttons=[
                    {"title": "📊 Estadísticas", "payload": "/stats"},
                    {"title": "⚙️ Configuración", "payload": "/config"},
                    {"title": "❓ Ayuda", "payload": "/help"}
                ]
            )
        elif platform == "facebook":
            # Funcionalidades específicas de Facebook
            dispatcher.utter_message(
                text="En Facebook Messenger tienes estas opciones:",
                buttons=[
                    {"title": "🛍️ Productos", "payload": "/products"},
                    {"title": "📞 Contacto", "payload": "/contact"},
                    {"title": "ℹ️ Info", "payload": "/info"}
                ]
            )
        else:
            dispatcher.utter_message(
                text="Funcionalidades disponibles en el bot",
                buttons=[
                    {"title": "Ayuda", "payload": "/help"},
                    {"title": "Info", "payload": "/info"}
                ]
            )

        return []


# Ejemplo de integración con APIs externas
class ActionGetWeather(Action):
    """Ejemplo de acción que consume una API externa."""

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Ejemplo básico - en producción usarías una API real
        try:
            # city = tracker.get_slot("city") or "Madrid"
            # Aquí harías la llamada real a una API del clima
            # response = requests.get(f"https://api.weather.com/v1/current/{city}")
            
            dispatcher.utter_message(
                text="🌤️ El clima hoy está soleado con 22°C (ejemplo)"
            )
        except Exception as e:
            dispatcher.utter_message(
                text="Lo siento, no pude obtener información del clima en este momento."
            )

        return []