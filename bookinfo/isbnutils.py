"""isbnutils wraps away the uglieness of crawling the amazon web page
"""

import urllib2
import cPickle as pickle

# cached lookups in a file
try:
    wcache=pickle.load(open('webcache.pickle','rb'))
except:
    wcache={}

# get url from web or cache, update cache
def __webget(url):
    if url in wcache:
        print "found url in cache: ", url
        return wcache[url]
   
    response = urllib2.urlopen(url)
    html = response.read()
    wcache[url] = html
    pickle.dump(wcache,open('webcache.pickle','wb'))
    return html

# returns all text between 'start' and 'end' strings 
def __between(text, start, end):
    s = text.find(start)+len(start)
    e = text.find(end, s)
    if s > 0 and e > 0:
        return text[s:e], text[e:]
    else:
        return '',text

def lookup(isbn):
    """Perform a lookup of the specified isbn number
    
    Args:
      isbn (str): The ISBN number. Both ISBN-10 and ISBN-13 is allowed.

    Returns:
      A dict mapping keys to the parsed data. For example:

      {'title': 'Cryptography Engineering: Design Principles and Practical Applications',
       'author': '',
       'keywords: []}
    """
    html = __webget('http://www.amazon.com/gp/search?keywords='+isbn)
    data_start = html.find('<div class="productData">')
    da,waste = __between(html[data_start:], '<div class="productTitle">', '</div>')
    title,da = __between(da, '>','<')
    auths,waste = __between(da, '<span class="ptBrand">by ','</span>')
    ret = {'title': title.strip(), 'author': auths.strip(), 'keywords': "" }
    return ret
