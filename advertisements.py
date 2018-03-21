import csv
import pandas as pd
import numpy as np

from helpers import truncatedRound

advertisements = pd.read_csv('./AdDetails.csv')

# Max distance to which flats are picked up based on degrees
MAX_DISTANCE = (1.0 / 111)

def getIndex(json, lat, lng):
  tLat = truncatedRound(lat)
  tLng = truncatedRound(lng)

  distances = []
  for circle in json['heatmaps']:
    srcLatLng = np.array([float(circle['lat']),float(circle['lng'])])
    destLatLng = np.array([tLat,tLng])
    distance = np.linalg.norm(srcLatLng-destLatLng)
    distances.append(distance)

  #print(np.min(distances), MAX_DISTANCE)

  if np.min(distances) < MAX_DISTANCE:
    return np.argmin(distances)
  else:
    return -1

def addAds(json):
  for i,advertisement in advertisements.iterrows():
    index = getIndex(json, advertisement['lat'], advertisement['lng'])

    if index == -1:
      continue

    if 'advertisements' not in json['heatmaps'][index]:
      json['heatmaps'][index]['advertisements'] = []

    data = {
      'name':advertisement['name'],
      'lat':advertisement['lat'],
      'lng':advertisement['lng'],
      'price':advertisement['price'],
      'img':advertisement['img'],
      'bhk':str(int(advertisement['bhk']))
    }

    #print(data)

    json['heatmaps'][index]['advertisements'].append(data)    
  
  return json
