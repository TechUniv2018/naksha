from gmaps import pollGmaps

def findNearby(req):
  '''
  Finds all the nearby places
  '''
  lat = req['lat']
  lng = req['lng']
  preferences = req['preferences']

  fetchedData = pollGmaps(lat, lng, preferences)
  
  return fetchedData
