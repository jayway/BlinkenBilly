"""isbnutils wraps away the uglieness of crawling the amazon web page
"""

import urllib2
import cPickle as pickle
from HTMLParser import HTMLParser

# cached lookups in a file
try:
    wcache=pickle.load(open('webcache.pickle','rb'))
except:
    wcache={}

# get url from web or cache, update cache
def __webget(url):
    if url in wcache:
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

    parser = AmazonProductParser()
    parser.feed(da) 
    return parser.title

def lookup(isbn):
    """Perform a lookup of the specified isbn number
    
    Args:
      isbn (str): The ISBN number. Both ISBN-10 and ISBN-13 is allowed.

    Returns:
      A dict mapping keys to the parsed data. For example:

      {'title': 'Cryptography Engineering: Design Principles and Practical Applications',
       'authors': ['Stephen Few'],
       'keywords: []}
    """

    # Discard some data
    html = __webget('http://www.amazon.com/gp/search?keywords='+isbn)
    data_start = html.find('<div class="productData">')
    data = html[data_start:]
    da,_ = __between(data, '<div class="productTitle">', '</div>')

    # Parse product data
    parser = AmazonProductParser()
    parser.feed(da)

    # Get result
    ret = {'title': parser.title, 'authors': parser.authors, 'keywords': "" }
    return ret

class AmazonProductParser(HTMLParser):
    def __init__(self):
        self.title = ""
        self.authors = []
        self.authorsBegin = False
        self.authorsEnd = False
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
        if tag == "span":
            if not self.authorsEnd:
                self.authorsBegin = True
                print "start authors start"

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
        if tag == "span":
            if self.authorsBegin:
                self.authorsEnd = True
                print "end authors done"
            
    def handle_data(self, data):
        print "Encountered some data  :", data
        # Assume title is always first
        if not self.title:
            self.title = data.strip()
        if self.authorsBegin and not self.authorsEnd:
            # Remove stupid "by", assume no author start name with it
            if data.startswith("by "):
                data = data[3:].strip()
            if data:
                self.authors.append(data.strip())
