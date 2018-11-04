import googlemaps
import sys
from access_token import token
token = token()
import time
import random
import json

def mapstest():
    args = sys.argv
    # location = (34.876615, -112.916040)

    start_time = time.time()
    gmaps = googlemaps.Client(key=token)

    type_counts = {}
    radius = 1500
    location = args[1:]
    print(location)
    # Expand the searching area's radius by 2 until 
    # there are at least 3 type of landmarks
    tries = 0
    while len(type_counts) == 0 or (len(type_counts) < 3 and tries < 3 and start_time + 3 > time.time()): 
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
    choice_indexes = sum([[index]*len(place['types']) for index, place in enumerate(places['results'])], [])
    # choices = sum([[key]*type_counts[key] for key in type_counts.keys()], [])

    # Make sure the final choices aren't the same
    from type_word_dictionary import type_word_dict
    final_choices = {}
    tries = 0
    while len(final_choices) < 3 and tries < 50:
        new_choice = places['results'][random.choice(choice_indexes)]
        if new_choice not in final_choices.values():
            new_choice['inspiration'] = random.choice(type_word_dict.get(random.choice(new_choice['types']), ['Not supported yet']))
            final_choices[len(final_choices)] = new_choice

        tries += 1

    python2json = json.dumps(final_choices)

    # print(inspiration)
    # print("Name", [c['name'] for c in final_choices])
    # print("Types", [c['types'] for c in final_choices])
    # print("Latitude, Longitude", [c['geometry']['location'] for c in final_choices])

    return python2json
