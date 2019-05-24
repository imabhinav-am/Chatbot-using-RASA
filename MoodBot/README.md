# Chatbot-using-RASA Deployed On Messenger
Creating a chatbot with Rasa stack and Python

Setup:

conda create --name bot python=3.6

source activate bot

python -m pip install rasa_nlu[spacy]

python -m pip install -U rasa_core

python -m spacy download en_core_web_md

python -m spacy link en_core_web_md en

./ngrok http 5004

For Visvualisation:

sudo apt-get -qq install -y graphviz libgraphviz-dev pkg-config

pip install pygraphviz

Talking To Bot

python -m rasa_core.run -d models/dialogue -u models/nlu/default/MoodBot
