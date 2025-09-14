# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
import datetime

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionHelloWorld(Action):
    """Simple custom action that says hello world."""

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="¡Hola! Esta es una acción personalizada.")

        return []


class ActionTellTime(Action):
    """Custom action to tell the current time."""

    def name(self) -> Text:
        return "action_tell_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        
        message = f"Son las {current_time} del {current_date}."
        
        dispatcher.utter_message(text=message)

        return []


class ValidateNameForm(FormValidationAction):
    """Validates the name form."""
    
    def name(self) -> Text:
        return "validate_name_form"
    
    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate name value."""
        
        if slot_value is None:
            return {"name": None}
        
        if isinstance(slot_value, str) and len(slot_value) < 2:
            dispatcher.utter_message(text="El nombre debe tener al menos 2 caracteres.")
            return {"name": None}
        else:
            return {"name": slot_value}