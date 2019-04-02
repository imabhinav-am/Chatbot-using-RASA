# Chatbot-using-RASA
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
