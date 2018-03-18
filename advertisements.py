import random
import csv

names = []

with open('./streets.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    names.append(row[0])

def addAds(json):
  SCALE = 1e-2
  for circle in json['heatmaps']:
    circle['advertisements'] = []
    for i, establishment in enumerate(circle['details']):
      index = random.randint(0, len(names)-1)
      location = establishment['geometry']['location']
      circle['advertisements'].append({
        'name': '%s APARTMENT'%(names[index]),
        'description': '3 BHK, price: 50,00,000 INR.',
        'lat': float(location['lat']) + (random.random() - .5) * SCALE,
        'lng': float(location['lng']) + (random.random() - .5) * SCALE
      })
  return json
