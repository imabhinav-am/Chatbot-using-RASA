from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

input_channel = FacebookInput(
    fb_verify="ResBot",
    # you need tell facebook this token, to confirm your URL
    fb_secret="f12e71394b4b95e1ae348a8023b72855",  # your app secret
    fb_access_token="EAAGH6Mgz3VoBAPX7ZCaOvbkNi6Y2qhKJ5ZBycstxdpYnEMr3LfOiqBksrrVNZAZA0FbxwilAyEhJa34EgczzHk9ZCPgC0KjAxroGuxd43xQjtaqv7v7kon1BH3L1S1pgV5G0zBjZCc5F75AS9aLXHpi7vEMUTQnaoHZBZAMe0JyM3eKKsykWfxhL"
    # token for the page you subscribed to
)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/ResBot')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

# set serve_forever=True if you want to keep the server running
s = agent.handle_channels([input_channel], 5004, serve_forever=True)
