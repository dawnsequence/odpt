'''Parse all data from place files into array and pickle it'''

import json
import os
import pickle

datadirectory='/Desktop/odpt/data/places/'

print os.listdir(datadirectory)[1]


'''update only where place_id matches between POI name and record name in places'''        
def joinDicttoList(inputlist, joindict, index="place_id"):
    for item in inputlist:
        try:
            if item[index]==joindict[index]:
                item.update(joindict)
                print item["place_id"], " was updated\n"
                #print item.keys()
                return inputlist
        except KeyError:
            print "no key ", index
            return None
        
    #return inputlist

def getPlaceInfoDict(placejson):
    placedict={}
    try:
        placedict["opening_hours"]=placejson["result"]["opening_hours"]["weekday_text"]
    except KeyError:
        placedict["opening_hours"]=''
    try:
        placedict["website"]=placejson["result"]["website"]
    except KeyError:
        placedict["website"]=''
    try:
        placedict["intl_phone_nr"]=placejson["result"]["international_phone_number"]
    except KeyError:
        placedict["intl_phone_nr"]=''
    try:
        placedict["review_count"]=len(placejson["result"]["reviews"])
    except KeyError:
        placedict["review_count"]=''
    try:
        placedict["place_id"]=placejson["result"]["place_id"]
    except KeyError:
        placedict["place_id"]='' 
        
    return placedict

#with open(datadirectory+os.listdir(datadirectory)[10]) as jsonfile:
##with open(os.listdir(datadirectory)[4]) as jsonfile:  #is just the file name
#    jsontext=json.load(jsonfile)
#jsonfile.close()
#
#jsontext=json.loads(jsontext)
#
#print getPlaceInfoDict(jsontext)

'''This part was used to dump all our places dicts to a file'''
#placesdicts=[]

#for jsonfile in (os.listdir(datadirectory))[1:]:
#    with open(datadirectory+jsonfile) as jsonfile:
#        jsontext=json.load(jsonfile)
#    jsonfile.close()
#    jsontext=json.loads(jsontext)
#    
#    poidict=getPlaceInfoDict(jsontext)
#    matches=0
#    for dictionary in placesdicts:
#        if poidict["place_id"] == dictionary["place_id"]:
#            matches+=1
#    
#    if matches==0:
#        placesdicts.append(poidict)
#        
#
##print placesdicts 
#print len(placesdicts)          

placesdictsdump='/Desktop/odpt/data/placesdictspickle.txt'
pickledatadir='/Desktop/odpt/data/POI/'
amuse='amusementpkl.txt'
shop='shopping_pkl.txt'
rest='restaurantpkl.txt'
park='parkpkl.txt'
museum='museumpkl.txt'
department='departmentpkl.txt'
cafe='cafepkl.txt'
art='art_pkl.txt'


'''All our type pickles'''
with open(pickledatadir+amuse, 'r') as pickleloc:
    amuselist=pickle.load(pickleloc)
pickleloc.close()

with open(pickledatadir+shop, 'r') as pickleloc:
    shoplist=pickle.load(pickleloc)
pickleloc.close()

with open(pickledatadir+rest, 'r') as pickleloc:
    restlist=pickle.load(pickleloc)
pickleloc.close()

with open(pickledatadir+park, 'r') as pickleloc:
    parklist=pickle.load(pickleloc)
pickleloc.close()

with open(pickledatadir+museum, 'r') as pickleloc:
    museumlist=pickle.load(pickleloc)
pickleloc.close()

with open(pickledatadir+department, 'r') as pickleloc:
    departmentlist=pickle.load(pickleloc)
pickleloc.close()

with open(pickledatadir+cafe, 'r') as pickleloc:
    cafelist=pickle.load(pickleloc)
pickleloc.close()

with open(pickledatadir+art, 'r') as pickleloc:
    artlist=pickle.load(pickleloc)
pickleloc.close()


with open(placesdictsdump, 'r') as places:
    placedicts=pickle.load(places)
places.close()

POIslist=[]
for x in artlist:
    POIslist.append(x)
for x in amuselist:
    POIslist.append(x)
for x in shoplist:
    POIslist.append(x)
for x in restlist:
    POIslist.append(x)
for x in parklist:
    POIslist.append(x)
for x in museumlist:
    POIslist.append(x)
for x in departmentlist:
    POIslist.append(x)
for x in cafelist:
    POIslist.append(x)

#print POIslist[30]
#print len(POIslist)
    

#amuselist=amuselist[0]
#joinDicttoList(placedicts, amuselist, index="place_id")

#for item in amuselist:
#    joinDicttoList(placedicts, item, index="place_id")

fullist=[]
#for item in placedicts:
#    if type(joinDicttoList(amuselist, item, index="place_id")) != type(None): #append only if it matched
#        fullist.append(joinDicttoList(amuselist, item, index="place_id"))
#    if type(joinDicttoList(shoplist, item, index="place_id")) != type(None): 
#        fullist.append(joinDicttoList(shoplist, item, index="place_id"))
#    if type(joinDicttoList(restlist, item, index="place_id")) != type(None): 
#        fullist.append(joinDicttoList(restlist, item, index="place_id"))
#    if type(joinDicttoList(shoplist, item, index="place_id")) != type(None): 
#        fullist.append(joinDicttoList(parklist, item, index="place_id"))
#    if type(joinDicttoList(parklist, item, index="place_id")) != type(None): 
#        fullist.append(joinDicttoList(museumlist, item, index="place_id"))
#    if type(joinDicttoList(museumlist, item, index="place_id")) != type(None): 
#        fullist.append(joinDicttoList(shoplist, item, index="place_id"))
#    if type(joinDicttoList(departmentlist, item, index="place_id")) != type(None): 
#        fullist.append(joinDicttoList(departmentlist, item, index="place_id"))
#    if type(joinDicttoList(cafelist, item, index="place_id")) != type(None): 
#        fullist.append(joinDicttoList(cafelist, item, index="place_id"))
#    if type(joinDicttoList(artlist, item, index="place_id")) != type(None): 
#        fullist.append(joinDicttoList(artlist, item, index="place_id"))

def rightJoin(listonleft, listtojoin, index):
    for i in listonleft:
        for j in listtojoin:
            if i[index]==j[index]:
                i.update(j)
        
    return listonleft

gr=rightJoin(placedicts, POIslist, "place_id")

print gr[0]
print len(gr)
    
        #for item in inputlist:
        #try:
        #    if item[index]==joindict[index]:
        #        item.update(joindict)
        #        print item["place_id"], " was updated\n"
        #        #print item.keys()
        #        return inputlist
        #except KeyError:
        #    print "no key ", index
        #    return None
    
a=[{"name":"cat", "age": 10}, {"name": "heidi", "age": 15}]
b=[{"name":"cat", "status": "awesome"}, {"name": "awful"}]

#print rightJoin(a, b, "name")

#for item in a:
#    print a.update(b)
        
#print len(placedicts)    
#print len(fullist)
#print len(amuselist), len(shoplist), len(restlist)
#
#
betterdump='/Desktop/odpt/data/betterpickle.txt'

with open(betterdump, 'wb') as placesdictsloc:
    pickle.dump(gr, placesdictsloc)
placesdictsloc.close()



