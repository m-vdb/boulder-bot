# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
import random
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher


TECHNIQUES = (
    "Edging",
    "Smearing",
    "Flagging",
    "Stemming",
    "Bat Hang",
    "Lay-Backing",
    "Mantle",
    "Undercling",
    "Drop Knee/Back Step",
    "Cross Through",
    "Side Pull",
    "Palming",
    "Dyno",
    "Heel Hook",
    "Toe Hook",
    "Lock-off",
    "Gaston",
)


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_list_random_techniques"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        techniques = random.choices(TECHNIQUES, k=5)
        dispatcher.utter_message(
            text=f"Here are some common bouldering techniques: {', '.join(techniques)}."
        )

        return []


class GymForm(FormAction):
    def name(self) -> Text:
        return "gym_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["gym_form_when", "gym_form_location"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        # utter submit template
        dispatcher.utter_message(text="Cool, you can go to Berta Block!")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """
        Map the slots to entities.
        """
        return {
            "gym_form_when": self.from_entity(entity="time"),
            "gym_form_location": self.from_entity(entity="GPE"),
        }
