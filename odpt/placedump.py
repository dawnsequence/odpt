'''
Reads places request files from a folder
1. If zero results, pass and go on to the next
2. If not zero, select first N from each category
3. Parses results from places file for these POIs into a list

Calls their details page based on google_id field
4. Parses results from details pages and adds to their results
5. Adds result lists to output Json file
6. Makes also 1 big table file from Json file

'''

import json
import os
import pickle

pf='C:/Users/liju/Desktop/odpt/Baigou.json'
pf2='C:/Users/liju/Desktop/odpt/Adachidaigochuugakkoumae.json'


# for y in os.listdir(testdir):
#     print y
# 
# dirlist=[y.split(".")[0] for y in os.listdir(testdir)]
# print dirlist

def hasResults(POIjsonfile):
    #print POIjsonfile["status"]
    if POIjsonfile["status"] == "OK":
        return 1
    else:
        return 0

    
def parsePOIfromPlaces(result, busstop_id=""):
    place={}
    place["busstop_id"]=busstop_id
    try:
        place["rating"]=result["rating"]
    except KeyError:
        place["rating"]=""
    try:
        place["name"]=result["name"]
    except KeyError:
        place["name"]=""
    try:
        place["place_id"]=result["place_id"]
    except KeyError:
        place["place_id"]=""
    try:
        place["coord"]=result["geometry"]["location"]
    except KeyError:
        place["coord"]=""
    try:
        place["types"]=result["types"]
    except KeyError:
        place["types"]=""
    try:
        place["price_level"]=result["price_level"]
    except KeyError:
        place["price_level"]=""
    try:
        place["photo_reference"]=result["photos"][0]["photo_reference"]
    except KeyError:
        place["photos"]=""
    
    return place    

def extractResultsFromPlace(POIjsonfile, maxnr, busstop_id):
    resultsarray=[]
    if len(POIjsonfile["results"]) <= maxnr:
        print "will extract all ", len(POIjsonfile["results"]), " results\n"
        for POI in POIjsonfile["results"][0:maxnr]:
            print POI["name"]
            POIdictionary=parsePOIfromPlaces(POI, busstop_id)
            if POIdictionary not in resultsarray:
                resultsarray.append(POIdictionary)
            else: pass
        print "\n"
    else:
        print "will extract up to ", maxnr, " results out of ", len(POIjsonfile["results"]), "\n"
        for POI in POIjsonfile["results"][0:maxnr]:
            print POI["name"]
            POIdictionary=parsePOIfromPlaces(POI, busstop_id)
            if POIdictionary not in resultsarray:
                resultsarray.append(POIdictionary)
            else: pass
        print "\n" 
    
    return resultsarray
    
    
def processPOIs(inputdir, maxnr):
    allPOI=[]
    hasresults=[]
    try:
        filenames=[POIfile.split(".")[0] for POIfile in os.listdir(inputdir)]
        if len(filenames)>0:
            for POIfile in filenames:
                with open(str(inputdir)+str(POIfile)+".json", "r") as jsonfile:
                    POIjson=json.load(jsonfile)
                jsonfile.close()
                #only need to do if double-JSON, which will be unicode
                if type(POIjson)==type(u'unicode'):
                    POIjson=json.loads(POIjson)
                #not empty
                if hasResults(POIjson):
                    hasresults.append(POIfile)
                    print POIfile, " has results and will be processed"
                    for result in extractResultsFromPlace(POIjson, maxnr, POIfile):
                        if result not in allPOI:
                            allPOI.append(result)
                        else:
                            pass
        #print len(allPOI), allPOI[0]["name"]
        print len(hasresults), " nonempty files processed"
        return allPOI            
            
            
    except KeyError:
        print "Give us a folder name, not an array or something"


testdir='C:/Users/liju/Desktop/odpt/tests/'
picklelocn='C:/Users/liju/Desktop/odpt/testdirpkl.txt'

departmentdir='C:/Users/liju/Desktop/odpt/data/department/'
departmentpicklelocn='C:/Users/liju/Desktop/odpt/data/POI/departmentpkl.txt'

print "\nStarting...\n\n"        
#testdirPOIlist=processPOIs(testdir, 2)

departmentPOI=processPOIs(departmentdir, 5)
#print len(testdirPOIlist), " results"
print len(departmentPOI), " POIs processed"
print departmentPOI[0]["name"]
#print testdirPOIlist[1]["name"]

fileobject=open(departmentpicklelocn, 'wb')
pickle.dump(departmentPOI, fileobject)
fileobject.close()
# # 
# fileobject=open(restaurantpicklelocn, 'r')
# restaurantresults=pickle.load(fileobject)
# fileobject.close()
# 
# print len(restaurantresults)
# print restaurantresults[0]


# for y in amusementresults:
#     print y

# processPOIs(dirlist)


