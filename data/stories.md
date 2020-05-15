## list grade systems
* greet
  - utter_greet
* grade_systems_list
  - utter_grade_systems_list

## detail of V scale
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

## gym form
* wanna_climb
    - gym_form
    - form{"name": "gym_form"}
    - slot{"gym_form_when": "today"}
    - slot{"gym_form_location": "berlin"}
    - form{"name": null}

## Wanna Climb today in Berlin

* greet
    - utter_greet
* wanna_climb
    - gym_form
    - form{"name":"gym_form"}
    - slot{"requested_slot":"gym_form_when"}
* inform{"time":"today"}
    - gym_form
    - slot{"gym_form_when":["2020-05-13T00:00:00.000+02:00","today"]}
    - slot{"requested_slot":"gym_form_location"}
* faq_system{"GPE":"Berlin"}
    - gym_form
    - slot{"gym_form_location":"Berlin"}
    - form{"name":null}
    - slot{"requested_slot":null}
