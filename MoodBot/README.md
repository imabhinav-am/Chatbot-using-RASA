# Chatbot-using-RASA Deployed On Messenger
Creating a chatbot with Rasa stack and Python

Setup:

conda create --name bot python=3.6

source activate bot

python -m pip install rasa_nlu[spacy]

python -m pip install -U rasa_core

python -m spacy download en_core_web_md

python -m spacy link en_core_web_md en

Ngrok
Ngrok is a multi-platform tunnelling, reverse proxy software that establishes secure tunnels from a public endpoint such as the internet to a locally running network service. In simple words it means, it opens access to your local app from the internet.

$ unzip /path/to/ngrok.zip

$ ../ngrok authtoken <token>

Start it by telling it which port we want to expose to the public internet : ./ngrok http 5004

For Visvualisation:

sudo apt-get -qq install -y graphviz libgraphviz-dev pkg-config

pip install pygraphviz

Make endpoints.yml as provided

Starting action server

python -m rasa_core_sdk.endpoint --actions action

Talking To Bot

python -m rasa_core.run -d models/dialogue -u models/nlu/default/MoodBot --endpoints endpoints.yml   

Deploying Bot on Messenger

How to get the FB credentials: You need to set up a Facebook app and a page.

To create the app head over to Facebook for Developers and click on My Apps -> Add New App.
Go onto the dashboard for the app and under Products, find the Messenger section and click Set Up. Scroll down to Token Generation and click on the link to create a new page for your app.
Create your page and select it in the dropdown menu for the Token Generation. The shown Page Access Token is the page-access-token needed later on.
Locate the App Secret in the app dashboard under Settings -> Basic. This will be your secret.
Use the collected secret and page-access-token in your credentials.yml, and add a field called verify containing a string of your choice. Start rasa_core.run with the --credentials credentials.yml option.
Set up a Webhook and select at least the messaging and messaging_postback subscriptions. Insert your callback URL which will look like https://<ngrok website>/webhooks/facebook/webhook. Insert the Verify Token which has to match the verify entry in your credentials.yml.

Run custom action(port 5055)
python -m rasa_core_sdk.endpoint --actions action

Now Run Server using app.py

python run_app.py


