## list grade systems
* greet
  - utter_greet
* grade_systems_list
  - utter_grade_systems_list

>> detail of V scale
  - ...
* faq_system
  - respond_faq_system

## compare grading systems
* compare_grade_systems
  - utter_systems_comparison

## list bouldering techniques
* list_bouldering_techniques
  - action_list_random_techniques

## thanks
* thanks
  - utter_your_welcome

## goodbye
* goodbye
  - utter_goodbye

>> Activate form 'gym_from'
  - ...
* wanna_climb
  - gym_form
  - form{"name": "gym_form"}

>> submit form
  - form{"name": "gym_form"}
  - ...
  - gym_form
  - form{"name": null}
  - slot{"requested_slot": null}
  - utter_submit_gym_form


>> fallback story
  - ...
* nlu_fallback
  - action_default_fallback
