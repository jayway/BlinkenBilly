"""General info 
"""

import isbnutils

class Isbn(object):
    """Represents a ISBN entry

    Attributes:
      isbn (str): The ISBN number.
      title (str): The title.
      author (list of str): List of authors.
      keywords (list of str): List of keywords.
      section (str): The section.

    """
    def __init__(self, isbn):
        """Create a new isbn instance.

        Args:
          isbn (str): The ISBN to make a lookup of.

        """
        self.isbn = isbn
        result = isbnutils.lookup(isbn)
        self.title = result['title']
        self.authors = result['authors']
        self.publication_date = "" 
        self.keywords = []
        self.section = ""
