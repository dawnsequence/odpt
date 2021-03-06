import json

bs='https://raw.githubusercontent.com/dawnsequence/odpt/master/busstops.json'
busstopsjson='/Desktop/odpt/busstops.json'
#busstops='https://raw.githubusercontent.com/misteroda/tokyo-odpt/master/data/bus_stops.json'
busroutes='https://raw.githubusercontent.com/misteroda/tokyo-odpt/master/data/bus_routes.json'
busroutesjson='/Desktop/odpt/busroutes.json'

placefile='/Desktop/odpt/Baigou.json'
placefile2='/Desktop/odpt/Adachidaigochuugakkoumae.json'
poifile='/Desktop/odpt/place-ChIJqSniv_qRGGAReerMAjODtSM.json'

# request=requests.get(busroutes)
# f=request.text
# 

def parsePlaces(localurl):
    
    with open(localurl, 'r') as jsonfile:
        placesjson=json.load(jsonfile)
    jsonfile.close()
    
    placesjson=json.loads(placesjson)
    print placesjson.keys()
    print len(placesjson["results"]), " results"
    
    resultslist=[]
    busstop_id=(placefile2.split("/")[-1]).split(".")[0]
    
    for result in placesjson["results"]:
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
        
        resultslist.append(place)
    
    return resultslist
    
    
with open(placefile, 'r') as jsonfile:
    busjson=json.load(jsonfile)

busjson=json.loads(busjson)
print busjson.keys()
print len(busjson["results"])
jsonfile.close()

busstop_id=(placefile2.split("/")[-1]).split(".")[0]
resultslist=[]
norating=[]
for result in busjson["results"]:
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
        

    resultslist.append(place)


for y in busjson["results"]:
    try:
        print y["name"]
        print y["geometry"]["location"]
        print y["place_id"]
        print y["types"]
        print y["photos"]
    except KeyError:
        print "none" 

print "one result: \n"   
print busjson["results"][1]    

for a in resultslist: 
    print a
    print "\n"
    
def detailsAPIgenerator(placeid):
    placeid=str(placeid)
    beforetag="https://maps.googleapis.com/maps/api/place/details/json?placeid="
    aftertag="&key= "
    finalrequest=beforetag+placeid+aftertag
    return finalrequest



placesarray=parsePlaces(placefile2)

print placesarray[2]["place_id"]

print detailsAPIgenerator(placesarray[2]["place_id"])

'''Make a list of place requests to call to get all the places'''
placerequests=[]
for x in placesarray:
    placerequests.append(detailsAPIgenerator(x["place_id"]))

#print placerequests


'''Parsing the POI info'''
#placesarray[2]
poifile='/Desktop/odpt/place-ChIJqSniv_qRGGAReerMAjODtSM.json'

with open(poifile, 'r') as jsonfile:
    poijson=json.load(jsonfile)
jsonfile.close()

print poijson.keys()
for y in poijson["result"]:
    print y

#of reviews
print len(poijson["result"]["reviews"])

#Monday opening hours
print poijson["result"]["opening_hours"]["weekday_text"][0]  

#website
print poijson["result"]["website"]

print poijson["result"]["international_phone_number"]

def parsePOIplace(localurl):
    
    with open(localurl, 'r') as jsonfile:
        poijson=json.load(jsonfile)
    jsonfile.close()
    
    print poijson.keys()
    for y in poijson["result"]: print y
    
    attributesdict={}
    try:
        attributesdict["review_count"]=len(poijson["result"]["reviews"])
    except KeyError:
        attributesdict["review_count"]=""
    try:
        attributesdict["website"]=poijson["result"]["website"]
    except KeyError:
        attributesdict["website"]=""
    try:
        attributesdict["international_phone_number"]=poijson["result"]["international_phone_number"]
    except KeyError:
        attributesdict["international_phone_number"]=""
    try:
        attributesdict["opening_hours"]=poijson["result"]["opening_hours"]["weekday_text"]
    except KeyError:
        attributesdict["opening_hours"]=""
    try:
        attributesdict["place_id"]=poijson["result"]["place_id"]
    except KeyError:
        attributesdict["place_id"]=''    
    
    return attributesdict

#Response of the parsing    
poidict=parsePOIplace(poifile)  
print poidict 

for item in poidict: print item
print poidict["opening_hours"][3]

print placesarray[2]

'''concatenate placesearch results matching dictionary
with dictionary for place details'''
# 
# for dictn in placesarray:
#     if dictn["place_id"]==poidict["place_id"]:
#         print "WE HAVE A MATCH"
#         print dictn
#         print poidict
#         dictn.update(poidict)
#         print "CONCATENATED DICTS\n"
#         print dictn
#         print dictn.keys()

print "\n"
print "\n"

'''update only where place_id matches between POI name and record name in places'''        
def joinDicttoList(inputlist, joindict, index="place_id"):
    for item in inputlist:
        try:
            if item[index]==joindict[index]:
                item.update(joindict)
                print item["place_id"], " was updated\n"
                print item.keys()
        except KeyError:
            print "no key ", index
        
    return inputlist

updatedlist=joinDicttoList(placesarray, poidict)
for i in updatedlist:
    print i, "\n"


'''updatedlist is the list we want to export now as final JSON'''

testlistfile='/Desktop/odpt/testlistexport.json'
asdicts='/Desktop/odpt/dictexport.json'

#dump to JSON file as a list of dictionaries
#better as just dictionaries?
with open(asdicts, 'w') as jsonfile:
    for i in updatedlist:
        json.dump(i, jsonfile)
    # json.dump(updatedlist, jsonfile)



#importing
# busjson=str(busjson)   #double-JSON encoding
# busjson=json.loads(busjson)  #loads uses string
    
# locations=busjson.keys()    
