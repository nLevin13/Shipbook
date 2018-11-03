import googlemaps
from access_token import token
token = token()
import time
import random

start_time = time.time()
gmaps = googlemaps.Client(key=token)

type_counts = {}
radius = 1500
location = (34.876615, -112.916040)

# Expand the searching area's radius by 2 until 
# there are at least 3 type of landmarks
tries = 0
while len(type_counts) == 0 or (len(type_counts) < 3 and tries < 5 and start_time + 5 > time.time()): 
    type_counts = {}
    places = gmaps.places_nearby(location=location, radius=radius)
    place_types = sum([p['types'] for p in places['results']],[])

    # Count total instances of each type
    type_counts = {}
    for ty in place_types:
        type_counts[ty] = type_counts.get(ty, 0) + 1
    radius *= 3
    tries += 1

# Choose three random types (weighted by frequency)
choices = []
choices = sum([[key]*type_counts[key] for key in type_counts.keys()], [])

# Make sure the final choices aren't the same
choice = []
tries = 0
while len(choice) < 3 and tries < 50:
    new_choice = random.choice(choices)
    if new_choice not in choice:
        choice.append(new_choice)
    tries += 1

# Use choices to pick words of inspiration~~~
from type_word_dictionary import type_word_dict
inspiration = [random.choice(type_word_dict.get(c, ['Not supported yet'])) for c in choice]

print(inspiration)
print(choice)
