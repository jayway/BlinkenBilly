#!/bin/python

# Extract the title and authors given an isbn by hitting amazon.

import urllib2
import cPickle as pickle

# cached lookups in a file
try:
 wcache=pickle.load(open('webcache.pickle','rb'))
except:
 wcache={}

# get url from web or cache, update cache
def webget(url):
 if url in wcache:
   print "found url in cache: ", url
   return wcache[url]
 else:
   response = urllib2.urlopen('http://www.amazon.com/gp/search?keywords='+isbn)
   html=response.read()
   wcache[url]=html
   pickle.dump(wcache,open('webcache.pickle','wb'))
   return html

def between(text, start, end):
 s=text.find(start)+len(start)
 e=text.find(end, s)
 if s > 0 and e > 0:
   return text[s:e], text[e:]
 else:
   print "not found"
   return '',text

def isbn_lookup(isbn):
 html=webget('http://www.amazon.com/gp/search?keywords='+isbn)
 data_start = html.find('<div class="productData">')
 da,waste=between(html[data_start:], '<div class="productTitle">', '</div>')
 title,da=between(da, '>','<')
 auths,waste=between(da, '<span class="ptBrand">by ','</span>')
 return title.strip(), auths.strip()

# read all isbns from file
isbns=[line.strip() for line in open('isbns.txt').readlines() if line.strip()]

# store the results as tuplse in a list
# (isbn, title, autors-string)
books=[]

# and lookup data for each
for isbn in isbns:
 t,a=isbn_lookup(isbn)
 print(isbn, t, a)
 books.append((isbn, t, a))

import pprint
pp=pprint.pprint
pp( books )

