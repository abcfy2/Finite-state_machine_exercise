#!/usr/bin/env python
# encoding: utf-8
# A sample for turnstile state
# for python 2.7 to python 3.4

state_table = {
        "locked":{
            "coin":{
                "next_state": "unlocked",
                "output": "Release turnstile so customer can push through"
                },
            "push":{
                "next_state": "locked",
                "output": None
                }
            },

        "unlocked":{
            "coin":{
                "next_state": "unlocked",
                "output": None
                },
            "push":{
                "next_state": "locked",
                "output": "When customer has pushed through lock turnstile"
                }
            }
        }

def get_next_state(current_state, act):
    print("current_state -> " + current_state + " , input -> " + act +":")
    state_get = state_table.get(current_state)
    if state_get and state_get.get(act):
        print("output --> " + str(state_get.get(act).get("output")))
        print("next_state --> " + state_get.get(act).get("next_state"))
        return state_get.get(act).get("next_state")
    else:
        print("invalid current_state or input.")
        return None

for current_state in ("locked", "unlocked", "unknown"):
    for act in ("coin", "push", "unknown"):
        get_next_state(current_state, act)
        print("-----------------------------------------\n")
