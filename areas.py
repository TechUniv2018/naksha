from gmaps import pollGmapsMock
from group import groupData

def findNearby(req):
  '''
  Finds all the nearby places
  '''
  lat = req['lat']
  lng = req['lng']
  preferences = req['preferences']

  fetchedData = pollGmapsMock(lat, lng, preferences)
  groupedData = groupData(fetchedData)
  
  return groupedData
