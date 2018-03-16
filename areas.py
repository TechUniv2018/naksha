from gmaps import pollGmaps
from group import groupData
from weights import getWeightedAreas 

def findNearby(req):
  '''
  Finds all the nearby places
  '''
  lat = req['lat']
  lng = req['lng']
  preferences = req['preferences']

  fetchedData = pollGmaps(lat, lng, preferences)
  groupedData = groupData(fetchedData)
  areas = getWeightedAreas(groupedData, preferences)
  
  return areas
