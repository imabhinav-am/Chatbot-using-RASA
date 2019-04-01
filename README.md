# Chatbot-using-RASA
Creating a chatbot with Rasa stack and Python

Setup:
conda create --name bot python=3.6
source activate bot
python -m pip install rasa_nlu
python -m pip install -U rasa_core
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en