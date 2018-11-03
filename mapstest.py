import googlemaps
from my_token import my_access_token
import random

gmaps = googlemaps.Client(key=my_access_token)
places = gmaps.places_nearby(location=(37.870569,-122.251584), radius=1500)
place_types = [p['types'] for p in places['results']]

#combine types
type_counts = {}
for place in place_types:
    for t in place:
        type_counts[t] = type_counts.get(t, 0) + 1

# Choose at most 3 random types
if len(type_counts.keys()) > 3:
    choices = []
    [choices.extend([[key]*type_counts[key] for key in type_counts.keys()])]
    choices = sum(choices, [])

    choice = []
    while len(choice) < 3:
        new_choice = random.choice(choices)
        if new_choice not in choice:
            choice.append(new_choice)
else:
    choice = list(type_counts.keys())

# Use choices to pick words of inspiration~~~
from type_word_dictionary import type_word_dict
inspiration = [random.choice(type_word_dict.get(c, ['Not supported yet'])) for c in choice]

print(inspiration)
