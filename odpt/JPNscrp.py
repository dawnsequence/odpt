# -*- coding: utf-8 -*-
'''docstring'''
import os
import urllib2
from bs4 import BeautifulSoup, Comment

LOCN = os.getcwd()+"/"+"tempscrape"+".txt"

SOURCEURL = "https://www.kotsu.metro.tokyo.jp/pickup_information/news/bus/index.html"
PAGE = urllib2.urlopen(SOURCEURL)
SOUP = BeautifulSoup(PAGE)

#print soup.prettify()

ddtags = SOUP.find_all("dd")
noncomments = SOUP.find_all(dds = lambda t: not isinstance(t, Comment))
for record in noncomments: 
	print record
ddstrings = []

for y in ddtags:
    ddstrings.append(unicode(y.string))
    
with open(LOCN, 'w') as outputFile:
    for y in ddstrings:
        outputFile.write(y.encode("utf-8")+"\n")
    outputFile.close()

os.startfile(LOCN)

# text=" ".join(dds.find_all(text=lambda t: not isinstance(t, Comment)))
# text=" ".join(text.split())
# print text
#print dds
# 
# for record in dds:
#      print record
#      print record.get('time datetime')
