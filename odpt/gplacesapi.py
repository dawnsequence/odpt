import csv
import json
import os
import sys
import requests
import urllib2
import numpy as np
import pickle


# print f


# 
requestedURL="https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&key= "
#r="A dict"
testfilename=' /Desktop/testjson.json'
placestest=' /Desktop/odpt/placestest.json'
busstopsjson=' /Desktop/odpt/busstops.json'
busroutesjson=' /Desktop/odpt/busroutes.json'
busstopscsv=' /Desktop/odpt/busstops.txt'
bs='https://raw.githubusercontent.com/dawnsequence/odpt/master/busstops.json'
#request=requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJrU31vOaHGGAR8RKvwt87QGU&key= ")
# request=requests.get(busroutes)
# f=request.text

'''Use these two methods to read/write json'''

'''save json result from gplaces API as json'''
# with open(testfilename, 'w') as jsonfile:
#     json.dump(f, jsonfile)
    
'''open json from gplaces API and read it'''    
# with open(testfilename, 'r') as jsonfile:
#     readjson=json.load(jsonfile)

    
# with open(busroutesjson, 'w') as jsonfile:
#     json.dump(f, jsonfile)

# jsonr=urllib2.urlopen(requestedURL)
# rjson=jsonr.read()
# readjson=json.load(urllib2.urlopen(requestedURL))


'''opening bus stops file'''
with open(busstopsjson, 'r') as jsonfile:
    busjson=json.load(jsonfile)
    
busjson=str(busjson)   #double-JSON encoding
busjson=json.loads(busjson)  #loads uses string
   
locations=busjson.keys()
print locations[1050]
print busjson[locations[1050]].keys()
print busjson[locations[1050]]['geo:lat'],",",busjson[locations[1050]]['geo:long']
print str(busjson[locations[1050]]['geo:lat'])+","+str(busjson[locations[1050]]['geo:long'])

# for y in locations:
#     print y.split(":")[1]

allstops= [(busjson[x]['geo:lat'], busjson[x]['geo:long'], x.split(":")[1], str(busjson[x]['geo:lat'])+","+str(busjson[x]['geo:long'])) for x in locations]

# with open(busstopscsv, 'wb') as csvfile:
#     writer=csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
#     
#     for y in allstops:
#         writer.writerow([y[2], y[3]])

       
def generatePlacesRequest(coordstring, POItype):
    
    beforetag='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
    aftertag='&radius=1000&rating%3E4&type='
    keytag='&key= '
    finalrequest=beforetag+str(coordstring)+aftertag+str(POItype)+keytag
    return finalrequest
           
new=generatePlacesRequest("-31.8670522,151.1957362", "restaurant") 
# rq=requests.get(new)
# rtest=rq.text
# 
# print rtest   

restaurantrequests=[]
caferequests=[]
barrequests=[]
tourrequests=[]
shoprequests=[]
#              
# for y in allstops:
#     restaurantrequests.append(generatePlacesRequest(y[3], "restaurant"))
#     caferequests.append(generatePlacesRequest(y[3], "cafe"))
#     caferequests.append(generatePlacesRequest(y[3], "bakery"))
#     barrequests.append(generatePlacesRequest(y[3], "bar"))
#     tourrequests.append(generatePlacesRequest(y[3], "park"))
#     tourrequests.append(generatePlacesRequest(y[3], "museum"))
#     tourrequests.append(generatePlacesRequest(y[3], "aquarium"))
#     tourrequests.append(generatePlacesRequest(y[3], "art_gallery"))
#     tourrequests.append(generatePlacesRequest(y[3], "amusement_park"))
#     shoprequests.append(generatePlacesRequest(y[3], "shopping_mall"))
#     shoprequests.append(generatePlacesRequest(y[3], "shoe_store"))
#     shoprequests.append(generatePlacesRequest(y[3], "store"))
#     shoprequests.append(generatePlacesRequest(y[3], "department_store"))
#     shoprequests.append(generatePlacesRequest(y[3], "clothing_store"))
# 
# print len(restaurantrequests), len(caferequests), len(barrequests), len(tourrequests), len(shoprequests)
# print tourrequests[0:5]    
        
# for y in allstops:
#     print y[0], y[1]
    
def euclideandistance(tuple1, tuple2):
    
    xdelt=tuple1[0] - tuple2[0]
    ydelt=tuple1[1] - tuple2[1]
    distance=np.sqrt(xdelt**2 + ydelt**2)
    distance=distance*100
    return distance
    

print euclideandistance((35.6624783, 139.7311523), (35.66325629, 139.8728754))

locns=[]
for y in allstops:
    locns.append(tuple([y[0], y[1]]))
    
#print locns

print euclideandistance(locns[0], locns[10]), locns[0], locns[10]
print euclideandistance(locns[0], locns[166]), locns[0], locns[166]
print len(locns)

distanceMatrix=np.zeros([len(locns), len(locns)])
matchMatrix=np.zeros([len(locns), len(locns)], dtype=int)

matchMatrix[0][0]=1888
print matchMatrix

counter=0
for row in distanceMatrix:
    i=0
    while i < len(row):
        row[i]=euclideandistance(locns[i], locns[counter])
        if row[i]<1.0:
            matchMatrix[i][counter]=0
        else:
            matchMatrix[i][counter]=int(row[i])
        i=i+1
    
    counter=counter+1
        
#print distanceMatrix[0]    
#print matchMatrix[0] 

def findDuplicates(inputmatrix):
    duplicates=[]
    counter=1
    for row in inputmatrix:
        i=counter
        while i<len(row):
            if row[i] < 1:
                print "Row: ", (counter-1), i
                duplicates.append((counter-1, i))
            i=i+1
        counter=counter+1
        
    return duplicates
    
dups=findDuplicates(matchMatrix)
unique=[]
print len(dups)

for row in dups:
    for entry in row:
        if entry not in unique:
            unique.append(entry)

print unique
print len(unique)

def getMatchDict(duplicatearray):
    matches={}
    count=0
    
    while count < len(duplicatearray) * 2:
        ary=[]
        for tup in duplicatearray:
            if tup[0] == count:
                ary.append(tup[1])
        if len(ary) > 0 : matches[count] = ary
        count=count+1
        
    return matches
    
matchdict=getMatchDict(dups)   

pkl=' /Desktop/odpt/busdictpickle.txt'

fileobject=open(pkl, 'wb')
pickle.dump(getMatchDict(matchdict), fileobject)
fileobject.close()
    
# matches=' /Desktop/odpt/busstopmatches.txt'            
# with open(matches, 'w') as outputFile:
#     for a in matchMatrix:
#         for b in a:
#             outputFile.write(str(b)+", ")
#         outputFile.write("|\n")
#     # for y in matchMatrix:
#     #     outputFile.write(str(y))
#         
#     outputFile.close()

    
# for x in locations:
#     print busjson[x]['geo:lat'], busjson[x]['geo:long'], x.split(":")[1]
# #print readjson['results'][0]['place_id']
        
#print readjson
# 
# print readjson.keys()
# print type(readjson.get("results")) #list
# 
# for a in readjson.get("results"):
#     print a
# #print readjson.values()
