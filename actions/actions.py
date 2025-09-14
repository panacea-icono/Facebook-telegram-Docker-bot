from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloDrTapia(Action):
    """Custom action that responds with a greeting to DR-TAPIA."""

    def name(self) -> Text:
        return "action_hello_dr_tapia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Send the custom greeting message
        dispatcher.utter_message(text="¡Hola, DR-TAPIA!")
        
        return []