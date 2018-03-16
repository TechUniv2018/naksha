import requests
import numpy as np
import json

# Radius in meters
RADIUS = 2500

# Gmaps key
with open('key.txt','r') as f:
    KEY = f.read()

def pollGmaps(lat, lng, preferences):
    '''
    Finds all places of type specified in preferences near lat, lng
    '''
    results = []
    for preference in preferences:
        location_type = preference['name']
        uri = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s,%s&radius=%s&type=%s&key=%s' \
              %(lat,lng,RADIUS,location_type,KEY)

    responseJson = requests.get(uri).json()
    results += responseJson['results']
    return results

def pollGmapsMock(a,b,c):
    '''
    Mocks the api call and retuns a saved response
    '''
    with open('./cache/raw_data.json','r') as f:
        return json.load(f)
