import numpy as np

with open('./types.txt','r') as f:
    types = f.read().split('\n')

inverseTypes = {}
for i, type_element in enumerate(types):
    inverseTypes[type_element] = i

def dot_product(preference, establishment):
    p = np.zeros(len(types))
    for type_element in preference:
        try:
            p[inverseTypes[type_element['name']]] = type_element['weight']
        except:
            pass
    
    e = np.zeros(len(types))
    if 'rating' in establishment:
        score = establishment['rating']
    else:
        score = 2.5
              
    for type_element in establishment['types']:
        try:
            e[inverseTypes[type_element]] = score
        except:
            pass

    return np.dot(p,e)
