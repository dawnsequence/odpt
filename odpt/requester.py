'''Gets page and dumps it as JSON'''

import pickle
import requests
import json
import time

restaurantrequestsfile='/Users/liju/Desktop/odpt/restaurantrequestspickle.txt'
coordsfile='C:/Users/liju/Dropbox/odpt/minimal_coords.txt'

'''use minimal and leftovers instead'''
restaurants_leftoverpickle='C:/Users/liju/Dropbox/odpt/restaurants_leftoverpickle.txt'
restaurants_minimalpickle='C:/Users/liju/Dropbox/odpt/restaurants_minimalpickle.txt'
shop_minimalpickle='C:/Users/liju/Dropbox/odpt/shop_minimalpickle.txt'
tour_minimalpickle='C:/Users/liju/Dropbox/odpt/tour_minimalpickle.txt'

# 
# fileobject=open(restaurantrequestsfile, 'r')
# restaurantrequests=pickle.load(fileobject)
# fileobject.close()
# print len(restaurantrequests)

fileobject=open(coordsfile, 'r')
coords=pickle.load(fileobject)
fileobject.close()
print "Coords file: ", len(coords), "first identifier: ", coords[0][0]

testvs=coords[:5]

testfilename='/Users/yulia/Desktop/odpt/places/restaurants/testid.txt'
#websitetoopen=restaurantrequests[0]
#print websitetoopen

print testvs
#prefix="/Users/yulia/Desktop/odpt/places/restaurants/"
prefix="/Users/liju/Desktop/odpt/data/amusement/"
        
def generatePlacesRequest(item, POItype):  
    beforetag='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
    #aftertag='&radius=1000&rating%3E3&type='
    aftertag='&radius=1000&type='
    keytag='&key=AIzaSyCkdHPOnGNLIicgC4lJaJucLjMVOxDPVUQ'
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
    department_store
    cafe
    shop
    museum
    park
    shopping_mall
'''    
#for item in coords:
#    identifier=item[0]
#    url = generatePlacesRequest(item[1], "restaurant")
#    #getRequestAndDump(url, identifier)

'''full list'''
'''
coords generated from:
    coordsfile='C:/Users/liju/Dropbox/odpt/minimal_coords.txt'
    with 469 records
    '''
for item in coords:
    url=generatePlacesRequest(item[1], "amusement_park")
    identifier=item[0]
    print item
    print url
    getRequestAndDump(url, identifier)
    time.sleep(10)

print len(coords), " coordinates to process"

# '''leftover list'''
# nextlist=[]
# 
# for item in coords[291:]:
#     print generatePlacesRequest(item[1], "restaurant")
#     print item
#     nextlist.append(item)
# 
# print "left: ", len(nextlist)
# 
# print "First identifier: ", nextlist[0][0]
# 
# 
# for item in nextlist:
#     url = generatePlacesRequest(item[1], "restaurant")
#     identifier = item[0] #identifier
#     print item
#     print url
#     #getRequestAndDump(url, identifier)
    
# 
# 
# counter=0
# endpoint=0
# for item in coords:
#     if 'Nishinipporirokuchoume' in item[0]:
#         print coords[counter], counter
#         endpoint=counter
#     counter+=1
# 
# print endpoint
# nextdaylist=coords[endpoint:]
# #print coords
# print nextdaylist[0], len(nextdaylist)
# 
# tester=nextdaylist[0]
# identifier=tester[0]
# url=generatePlacesRequest(tester[1], "restaurant")
# getRequestAndDump(url, identifier)

# testitem=nextdaylist[0]
# testurl=generatePlacesRequest(testitem[1], "cafe")
# print testitem[0], testurl
# getRequestAndDump(testurl, testitem[0])
print "Start again\n\n"
# for item in nextdaylist[1:]:
#     print item
# 
# newrequests=[]    
# for item in nextdaylist[4:]:
#     identifier=item[0]
#     url = generatePlacesRequest(item[1], "restaurant")
#     newrequests.append(url)
#     #print url, identifier
#     #getRequestAndDump(url, identifier)
#     
# countr=0

print coords[291] #Nishiojiekimae

#Use leftovers-busstops.csv for the rest of the busstops list
#from next on, load busstops from minimal.csv
# for i in nextdaylist[4:10]:
#     #print nextdaylist[counter]
#     print i
#     print newrequests[countr]
#     countr+=1