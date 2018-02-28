'''

Calls their details page based on google_id field
4. Parses results from details pages and adds to their results
5. Adds result lists to output Json file
6. Makes also 1 big table file from Json file

'''
import json
import pickle
import requests
import time

def detailsCallgenerator(place_id):
    placeid=str(place_id)
    beforetag="https://maps.googleapis.com/maps/api/place/details/json?placeid="
    aftertag="&key=AIzaSyCkdHPOnGNLIicgC4lJaJucLjMVOxDPVUQ"
    finalrequest=beforetag+placeid+aftertag
    return finalrequest
    
def getRequestAndDump(url, identifier, prefix='C:/Users/liju/Desktop/odpt/data/places/', delay=30):
    print url
    request=requests.get(url)
    responsebody=request.text
    
    filename=prefix+identifier+".json"
    with open(filename, 'w') as jsonfile:
        json.dump(responsebody, jsonfile)
    jsonfile.close()
    #time.sleep(delay)

picklelocn='C:/Users/liju/Desktop/odpt/data/POI/departmentpkl.txt'

fileobject=open(picklelocn, 'r')
testresults=pickle.load(fileobject)
fileobject.close()

for y in testresults:
    print y["place_id"]
    callurl=detailsCallgenerator(y["place_id"])
    getRequestAndDump(callurl, y["place_id"])