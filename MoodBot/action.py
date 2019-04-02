from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.events import SlotSet
from IPython.core.display import Image, display

import logging
import requests
import json
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)

import requests

class ApiAction(Action):
    def name(self):
        return "action_retrieve_image"

    def run(self, dispatcher, tracker, domain):
        
        group = tracker.get_slot('group')
        #print(group)
        r = requests.get('http://shibe.online/api/{}?count=1&urls=true&httpsUrls=true'.format(group))
        response = r.content.decode()
        response = response.replace('["',"")
        response = response.replace('"]',"")
   
        
        #display(Image(response[0], height=550, width=520))
        dispatcher.utter_message("Here is something to cheer you up: {}".format(response))
        
        # request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        # joke = request['value']  # extract a joke from returned json response
        # dispatcher.utter_message(joke)  # send the message back to the user
        
        return []
