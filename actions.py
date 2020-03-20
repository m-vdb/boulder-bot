# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
import random
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
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
        dispatcher.utter_message(text=f"Here are some common bouldering techniques: {', '.join(techniques)}.")

        return []
