#!/usr/bin/env python
# coding: utf-8

# In[65]:


get_ipython().run_line_magic('matplotlib', 'inline')

import logging, io, json, warnings
logging.basicConfig(level="INFO")
warnings.filterwarnings('ignore')


# In[66]:


import rasa_nlu
import rasa_core
import spacy


# In[67]:


#nlu.md and #stories.md provided


# In[68]:


from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

# loading the nlu training samples
training_data = load_data("nlu.md")

# trainer to educate our pipeline
trainer = Trainer(config.load("config.yml"))

# training the model
interpreter = trainer.train(training_data)

# store it for future use
model_directory = trainer.persist("./models/nlu", fixed_model_name="ResBot")


# In[69]:


#stories.md and domain.yml provided


# In[70]:


get_ipython().system('python -m rasa_core.visualize -s stories.md -d domain.yml -o story_graph.html')


# In[32]:


#!python -m rasa_nlu.train -c config.yml --fixed_model_name ResBot --data nlu.md -o models --project nlu --verbose


# In[36]:


get_ipython().system('python -m rasa_core.train interactive -s stories.md --nlu models/nlu/ResBot -d domain.yml -o models/dialogue --verbose --endpoints endpoints.yml')


# In[71]:


from rasa_core.policies import KerasPolicy, MemoizationPolicy, FormPolicy
from rasa_core.agent import Agent

agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy(batch_size=100, epochs=500,
                                             validation_split=0.2), FormPolicy()])

# loading our neatly defined training dialogues
training_data = agent.load_data('stories.md')

agent.train(training_data)

agent.persist('models/dialogue')


# In[ ]:





# In[ ]:




