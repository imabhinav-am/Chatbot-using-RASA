#Resturant Bot using RASA Stack For booking Resturant

For Interactive training:

!python -m rasa_core.train interactive -s stories.md --nlu models/nlu/ResBot -d domain.yml -o models/dialogue --verbose --endpoints endpoints.yml

For Running Bot
python -m rasa_core.run --core models/dialogue --nlu models/nlu/default/ResBot --verbose --endpoints endpoints.yml

Note: First try to develop MoodBot.
