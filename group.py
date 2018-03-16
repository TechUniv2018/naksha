def groupData(fetchedData):
  '''
  Groups the data by truncating lat and lng
  '''
  newGroup = {}

  # Resolution of the result
  RESOLUTION = 100
  truncatedRound = lambda x: round(float(x) * RESOLUTION) / RESOLUTION

  def processResult(result):
      lat = result['geometry']['location']['lat']
      lng = result['geometry']['location']['lng']

      lat = truncatedRound(lat)
      lng = truncatedRound(lng)

      if lat not in newGroup:
          newGroup[lat] = {}
      if lng not in newGroup[lat]:
          newGroup[lat][lng] = {}

      newGroup[lat][lng][result['place_id']] = result

  for establishment in fetchedData:
      processResult(establishment)
  
  return newGroup
