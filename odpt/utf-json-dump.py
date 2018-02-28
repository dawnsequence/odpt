import pickle
import unicodecsv as ucsv
import csv
import json

# pickloc='C:/Users/liju/Desktop/odpt/data/betterpickle.txt'
# 
# with open(pickloc, 'r') as pickl:
#     fullarray=pickle.load(pickl)
# pickl.close()
# 
# print len(fullarray)
# 
# with open('C:/Users/liju/Desktop/odpt/data/allcsvkeys.csv', 'wb') as f:
#     f.write(u'\ufeff'.encode('utf8'))
#     writer=csv.writer(f)
#     writer.writerow(fullarray[0].keys())
#     for item in fullarray:
#         writer.writerow(item.values())
#         
# f.close()

fileloc='C:/Users/liju/Dropbox/odpt/data/odpt-POI-(!header).csv'
with open(fileloc, 'r') as filel:
    reader=csv.reader(filel)
    lst=list(map(tuple, reader))
filel.close()

print lst[0]

fullist=[]

for item in lst:
    itemdict={}
    itemdict["place_id"]=item[0]
    itemdict["lat"]=item[1]
    itemdict["lon"]=item[2]
    itemdict["name"]=item[3]
    itemdict["rating"]=item[4]
    itemdict["intl_phone_nr"]=item[5]
    itemdict["review_count"]=item[6]
    itemdict["busstop_id"]=item[7]
    itemdict["price_level"]=item[8]
    itemdict["opening_hours"]=item[9]
    itemdict["website"]=item[10]
    itemdict["photo_reference"]=item[11]
    itemdict["types"]=item[12]
    itemdict["full_busstop_id"]=item[13]
    fullist.append(itemdict)
print fullist, len(fullist)
print fullist[1]

floc='C:/Users/liju/Desktop/odpt/data/long-buses.txt'
with open(floc, 'wb') as pklfile:
    pickle.dump(fullist, pklfile)
pklfile.close()

with open(floc, 'r') as pklfile:
    unpickled=pickle.load(pklfile)
pklfile.close()

jloc='C:/Users/liju/Desktop/odpt/data/long-buses.json'
with open(jloc, 'wb') as jsonfile:
    jsonfile.write(json.dumps(unpickled, ensure_ascii=False))

jsonfile.close()
