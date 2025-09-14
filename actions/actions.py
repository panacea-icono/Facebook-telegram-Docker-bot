# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


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


class ValidateNameForm(FormAction):
    """Validates the name form."""
    
    def name(self) -> Text:
        return "validate_name_form"
        
    def required_slots(self, domain_slots: List[Text],
                      dispatcher: CollectingDispatcher,
                      tracker: Tracker,
                      domain: Dict[Text, Any]) -> List[Text]:
        return ["name"]
    
    def slot_mappings(self) -> Dict[Text, Any]:
        return {"name": self.from_entity(entity="name", not_intent="chitchat")}

    def validate_name(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Dict[Text, Any]:
        """Validate name value."""
        if len(value) < 2:
            dispatcher.utter_message(text="El nombre debe tener al menos 2 caracteres.")
            return {"name": None}
        else:
            return {"name": value}

    def submit(self,
              dispatcher: CollectingDispatcher,
              tracker: Tracker,
              domain: Dict[Text, Any]) -> List[Dict]:
        """Submit the form."""
        name = tracker.get_slot("name")
        dispatcher.utter_message(text=f"¡Encantado de conocerte, {name}!")
        return []