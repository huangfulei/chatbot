# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
#
# class ValidateOrderForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_order_form"
#
#     async def validate_email(
#             self,
#             value: Text,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         if value:
#             print('this is the value', value)
#             return {"confirm_exercise": True}
#         else:
#             print('this is the value: ', value)
#             return {"exercise": "None", "confirm_exercise": False}
#

class ActionSubmitResults(Action):
    def name(self) -> Text:
        return "action_submit_results"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        email = tracker.get_slot("email")
        payment_method = tracker.get_slot("payment_method")

        print('email is: ', email)
        print('payment method is: ', payment_method)

        dispatcher.utter_message("Thanks, your order has been placed!")
        return []
