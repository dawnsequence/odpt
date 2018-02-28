'''loads the json files from the requests'''

import json

testfilename='/Desktop/odpt/places/restaurants/testid.txt'

with open(testfilename, 'r') as jsonfile:
    busjson=json.load(jsonfile)

jsonfile.close()

#busjson=str(busjson)   #double-JSON encoding
busjson=json.loads(busjson)
    
print busjson.keys()
print busjson.values()

prefix="/Desktop/odpt/places/restaurants/"
identifier="ehwah"
filename=prefix+identifier+".txt"

print filename