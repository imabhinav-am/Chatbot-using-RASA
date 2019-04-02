from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

input_channel = FacebookInput(
    fb_verify="<any string>",
    # you need tell facebook this token, to confirm your URL
    fb_secret="",  # your app secret
    fb_access_token=""
    # token for the page you subscribed to
)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/MoodBot')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

# set serve_forever=True if you want to keep the server running
s = agent.handle_channels([input_channel], 5004, serve_forever=True)
