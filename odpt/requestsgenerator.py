'''generate google api requests'''

import csv
import pickle

#csvfileloc='/Users/yulia/Desktop/odpt/firstID.csv'
csvfileloc='C:/Users/liju/Dropbox/odpt/leftovers-busstops.csv'
minimalbuses='C:/Users/liju/Dropbox/odpt/minimal.csv'
leftoverbuses='C:/Users/liju/Dropbox/odpt/leftovers-busstops.csv'

def generatePlacesRequest(coordstring, POItype):
    
    beforetag='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
    aftertag='&radius=1000&rating%3E4&type='
    keytag='&key=AIzaSyCkdHPOnGNLIicgC4lJaJucLjMVOxDPVUQ'
    finalrequest=beforetag+str(coordstring)+aftertag+str(POItype)+keytag
    return finalrequest
           
new=generatePlacesRequest("-31.8670522,151.1957362", "restaurant") 
requestidlist=[]
requestcoordslist=[]

with open(csvfileloc, 'r') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    
    for row in reader:
        #requestidlist.append(row[0])
        #requestcoordslist.append(row[1])
        requestcoordslist.append([row[0], row[1]])

#list of coordinates to make our places request on        
print requestcoordslist
print len(requestcoordslist)
requestcoordslist=requestcoordslist[0:]
requestidlist=requestidlist[0:]
#print len(requestcoordslist), len(requestidlist)
print requestcoordslist[0]
print requestcoordslist[-1]

restaurantrequests=[]
caferequests=[]
#barrequests=[]
tourrequests=[]
shoprequests=[]

for stop in requestcoordslist:
    restaurantrequests.append(generatePlacesRequest(stop[1], "restaurant"))
    #caferequests.append(generatePlacesRequest(stop[1], "cafe"))
#     caferequests.append(generatePlacesRequest(y[3], "bakery"))
#     barrequests.append(generatePlacesRequest(y[3], "bar"))
#     tourrequests.append(generatePlacesRequest(stop[1], "park"))
#     tourrequests.append(generatePlacesRequest(stop[1], "museum"))
# #     tourrequests.append(generatePlacesRequest(y[3], "aquarium"))
# #     tourrequests.append(generatePlacesRequest(y[3], "art_gallery"))
# #     tourrequests.append(generatePlacesRequest(y[3], "amusement_park"))
#     shoprequests.append(generatePlacesRequest(stop[1], "shopping_mall"))
# #     shoprequests.append(generatePlacesRequest(y[3], "shoe_store"))
# #     shoprequests.append(generatePlacesRequest(y[3], "store"))
#     shoprequests.append(generatePlacesRequest(stop[1], "department_store"))
#     shoprequests.append(generatePlacesRequest(y[3], "clothing_store"))
# 
print len(restaurantrequests)
# len(caferequests), len(tourrequests), len(shoprequests)
print restaurantrequests[0]
print restaurantrequests[-1]
# print tourrequests[0:5]

#print len(restaurantrequests)
#print tourrequests[0]
#print caferequests[0]
#print shoprequests[0]
#print restaurantrequests[0]

shoprequestsfile='/Users/yulia/Desktop/odpt/shoprequestspickle.txt'
caferequestsfile='/Users/yulia/Desktop/odpt/caferequestspickle.txt'
tourrequestsfile='/Users/yulia/Desktop/odpt/tourrequestspickle.txt'
restaurantrequestsfile='/Users/yulia/Desktop/odpt/restaurantrequestspickle.txt'
coordsfile='/Users/yulia/Desktop/odpt/ids-coords-pickle.txt'

restaurants_leftoverpickle='C:/Users/liju/Dropbox/odpt/restaurants_leftoverpickle.txt'
restaurants_minimalpickle='C:/Users/liju/Dropbox/odpt/restaurants_minimalpickle'

#fileobject=open(shoprequestsfile, 'wb')
#pickle.dump(shoprequests, fileobject)
#fileobject.close()
#
#fileobject=open(caferequestsfile, 'wb')
#pickle.dump(caferequests, fileobject)
#fileobject.close()
#
#fileobject=open(tourrequestsfile, 'wb')
#pickle.dump(tourrequests, fileobject)
#fileobject.close()
#
fileobject=open(restaurants_leftoverpickle, 'wb')
pickle.dump(restaurantrequests, fileobject)
fileobject.close()

# fileobject=open(coordsfile, 'wb')
# pickle.dump(requestcoordslist, fileobject)
# fileobject.close()

# 
# fileobject=open(tourrequestsfile, 'r')
# b=pickle.load(fileobject)
# print b[2]




