import numpy as np
import sys
import pickle

a=np.zeros([10, 10])
b=np.zeros([10, 10])
print a[5][7]
#print a

def euclideandistance(tuple1, tuple2):
    
    xdelt=tuple1[0] - tuple2[0]
    ydelt=tuple1[1] - tuple2[1]
    distance=np.sqrt(xdelt**2 + ydelt**2)
    distance=distance*100
    return distance

testvec=[(35.77289171, 139.7391417), (35.72590603, 139.66773), (35.77407769, 139.740344), (35.70381727, 139.8143967), (35.65036784, 139.8075825), (35.67895074, 139.8272884), (35.70255425, 139.8645367), (35.72859809, 139.661569), (35.72857313, 139.6615191), (35.70210395, 139.8638292)]
print len(testvec)

counter=0
print a

for r in a:
    i=0
    
    while i<len(r):
        r[i]=euclideandistance(testvec[i], testvec[counter])
        print r[i]
        if r[i]<1.0:
            b[i][counter]=0
        else:
            b[i][counter]=int(r[i])
        i=i+1
    # print r
    # for sub in r:
    #     sub=euclideandistance(testvec[i], testvec[counter])
    #     i=i+1
    #     print sub
    
    counter=counter+1
    
for f in a:
    for n in f:
        print '{:.3f}'.format(float(n))


cy=0        

print a   
print b

# printtest='/Desktop/odpt/printtest.txt'            
# with open(printtest, 'w') as outputFile:
#         outputFile.write(str(a))
#         outputFile.write(str(b)) 
#         outputFile.close()

duplicates=[]
counter=1
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
    
# for x in b:
#     i=counter
#     while i<len(b):
#         if x[i]<1:
#             print "Row: ", (counter-1), i
#             duplicates.append((counter-1, i))
#         i=i+1
#     
#     counter=counter+1
    
dus=findDuplicates(b)    
    
f=b[0:len(b)/2, 0:len(b)]
print f 

unique=[]
for f in dus:
    for y in f:
        if y not in unique:
            unique.append(y)

print dus            
print unique
matches={}
count=0

while count < len(dus)*2:
    ary=[]
    print "Count: ", count
    for y in dus:
        if y[0]==count:
            ary.append(y[1])
    print ary
    if len(ary)> 0: matches[count]=ary    
    count=count+1
    
print matches

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
    
print getMatchDict(dus)

filename='/Desktop/odpt/busdictpickle.txt'

fileobject=open(filename, 'wb')
pickle.dump(getMatchDict(dus), fileobject)
fileobject.close()

fileobject=open(filename, 'r')
b=pickle.load(fileobject)
print b


    
        
    
