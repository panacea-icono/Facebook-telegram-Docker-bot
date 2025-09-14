from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHola(Action):
    """Acción personalizada que responde con un saludo específico a DR-TAPIA"""

    def name(self) -> Text:
        return "action_hola"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Respuesta personalizada para DR-TAPIA
        message = "¡Hola, DR-TAPIA! Soy tu bot multicanal Rasa 🤖"
        
        # Enviar el mensaje al usuario
        dispatcher.utter_message(text=message)
        
        return []