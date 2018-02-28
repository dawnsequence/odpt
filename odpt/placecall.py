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
import os

def detailsCallgenerator(place_id):
    placeid=str(place_id)
    beforetag="https://maps.googleapis.com/maps/api/place/details/json?placeid="
    #aftertag="&key=AIzaSyCkdHPOnGNLIicgC4lJaJucLjMVOxDPVUQ"
    #aftertag="&key=AIzaSyA1juD_DrcPs36qAyb5OHtQZ3ezh6VdBJs"
    aftertag="&key=AIzaSyCLvhZZ6OJbvikK0GcJQpM4BKJ6dnq4Vgk"
    finalrequest=beforetag+placeid+aftertag
    return finalrequest
    
def getRequestAndDump(url, identifier, prefix='/Users/yulia/Desktop/odpt/data/places/', delay=0):
    #print url
    request=requests.get(url)
    responsebody=request.text
    
    forStatusCheck=json.loads(responsebody)
    print forStatusCheck["status"]
    if forStatusCheck["status"]=="OK":   
        filename=prefix+identifier+".json"
        with open(filename, 'w') as jsonfile:
            json.dump(responsebody, jsonfile)
        jsonfile.close()
    time.sleep(delay)

picklelocn='/Users/yulia/Desktop/odpt/data/POI/departmentpkl.txt'
testdir='/Users/yulia/Desktop/odpt/data/POI/'

fileobject=open(picklelocn, 'r')
testresults=pickle.load(fileobject)
fileobject.close()

print len(testresults)
uniqueplaces=[]
allplaces=[]

#for y in os.listdir(testdir):
#    fileobject=open(testdir+y, 'r')
#    picklecontent=pickle.load(fileobject)
#    fileobject.close()
#    for item in picklecontent:
#        allplaces.append(item["place_id"])
#        if item["place_id"] not in uniqueplaces:
#            uniqueplaces.append(item["place_id"])
#        
#print len(allplaces), len(uniqueplaces)

uniquepickle='/Users/yulia/Desktop/odpt/data/POI/unique.txt'

#fileobject=open(uniquepickle, 'wb')
#pickle.dump(uniqueplaces, fileobject)
#fileobject.close()

fileobject=open(uniquepickle, 'r')
uniques=pickle.load(fileobject)
fileobject.close()

outputlocn='/Users/yulia/Desktop/odpt/data/places/'

print uniques[0]
print type((os.listdir(outputlocn))[1])
print os.listdir(outputlocn)[0]
print uniques[0]+".json" in os.listdir(outputlocn)

currentindex=0 
numbernotok=0
#for uniqueID in uniques:
#    callurl=detailsCallgenerator(uniqueID)
#    if uniqueID+".json" not in os.listdir(outputlocn):
#        getRequestAndDump(callurl, uniqueID, delay=0)
#        numbernotok+=1
#    else:
#        pass
#    currentindex+=1
#    print currentindex, uniqueID
#    #print callurl
#
#print len(uniques), numbernotok

#testurl=detailsCallgenerator(uniques[0])
#getRequestAndDump(testurl, uniques[0])       
             
#for y in testresults:
#    print y["place_id"]
#    callurl=detailsCallgenerator(y["place_id"])
#    #getRequestAndDump(callurl, y["place_id"])