import csv
import pandas as pd
import numpy as np

from helpers import truncatedRound

advertisements = pd.read_csv('./AdDetails.csv')

def getIndex(json, lat, lng):
  tLat = truncatedRound(lat)
  tLng = truncatedRound(lng)

  distances = []
  for circle in json['heatmaps']:
    srcLatLng = np.array([float(circle['lat']),float(circle['lng'])])
    destLatLng = np.array([tLat,tLng])
    distance = np.linalg.norm(srcLatLng-destLatLng)
    distances.append(distance)

  return np.argmin(distances)

def addAds(json):
  for i,advertisement in advertisements.iterrows():
    index = getIndex(json, advertisement['lat'], advertisement['lng'])

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

    print(data)

    json['heatmaps'][index]['advertisements'].append(data)    
  
  return json

