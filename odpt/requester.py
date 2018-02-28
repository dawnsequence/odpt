'''Gets page and dumps it as JSON'''

import pickle
import requests
import json
import time

restaurantrequestsfile='/Users/yulia/Desktop/odpt/restaurantrequestspickle.txt'
#coordsfile='/Users/yulia/Desktop/odpt/ids-coords-pickle.txt'
coordsfile='/Users/yulia/Dropbox/odpt/minimal_coords.txt'

fileobject=open(restaurantrequestsfile, 'r')
restaurantrequests=pickle.load(fileobject)
fileobject.close()
print len(restaurantrequests)

fileobject=open(coordsfile, 'r')
coords=pickle.load(fileobject)
fileobject.close()
print len(coords), coords[0][0]

#testvs=coords[:5]
#
#
#testfilename='/Users/yulia/Desktop/odpt/places/restaurants/testid.txt'
#websitetoopen=restaurantrequests[0]
#print websitetoopen


#
#print testvs
prefix="/Users/yulia/Desktop/odpt/data/aquarium/"
        
def generatePlacesRequest(item, POItype):  
    beforetag='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
    aftertag='&radius=2000&rating%3E3&type='
    #aftertag='&radius=1000&type='
    #keytag='&key=AIzaSyCkdHPOnGNLIicgC4lJaJucLjMVOxDPVUQ'
    keytag='&key=AIzaSyA1juD_DrcPs36qAyb5OHtQZ3ezh6VdBJs'
    finalrequest=beforetag+str(item)+aftertag+str(POItype)+keytag
    return finalrequest
        
def getRequestAndDump(url, identifier):
    print url, identifier
    request=requests.get(url)
    responsebody=request.text
    
    filename=prefix+identifier+".json"
    with open(filename, 'w') as jsonfile:
        json.dump(responsebody, jsonfile)
    jsonfile.close()


'''Use this to get responses: uncomment again when quota released
Additional categories: 
    -department_store
    -cafe
    shop
    museum
    -park
    -shopping_mall
    -art_gallery
'''    
#for item in coords:
#    identifier=item[0]
#    url = generatePlacesRequest(item[1], "restaurant")
#    #getRequestAndDump(url, identifier)

#for item in coords[0:6]:
#    print item
#
#counter=0
#endpoint=0
#for item in coords:
#    if 'Nishinipporirokuchoume' in item[0]:
#        print coords[counter], counter
#        endpoint=counter
#    counter+=1
#
#print endpoint
#nextdaylist=coords[endpoint:]
##print coords
#print nextdaylist[0], len(nextdaylist)

#tester=nextdaylist[0]
#identifier=tester[0]
#url=generatePlacesRequest(tester[1], "restaurant")
#getRequestAndDump(url, identifier)

for item in coords[114:]:
    identifier=item[0]
    url = generatePlacesRequest(item[1], "aquarium")
    print url, identifier
    getRequestAndDump(url, identifier)
    time.sleep(100)
    
#print coords[113]