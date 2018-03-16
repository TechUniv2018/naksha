import random

def addAds(json):
  json['advertisements'] = []
  for circle in json['heatmaps']:
    for i, establishment in enumerate(circle['details']):
      location = establishment['geometry']['location']
      json['advertisements'].append({
        'name': 'Placeholder Apartment %s'%(i),
        'description': '3 BHK, price: 50,00,000 INR, Placeholder description.',
        'lat': float(location['lat']) + (random.random() - .5),
        'lng': float(location['lng']) + (random.random() - .5)
      })
  return json