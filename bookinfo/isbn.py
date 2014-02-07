"""General info 
"""

class Isbn(object):
    """Represents a ISBN entry

    Attributes:
      isbn (str): The ISBN number.
      title (str): The title.
      author (str): The author.
      keywords (list of str): List of keywords.
      section (str): The section.

    """
    def __init__(self, isbn):
        """Create a new isbn instance.

        Args:
          isbn (str): The ISBN to make a lookup of.

        """
        self.isbn = isbn
        self.title = ""
        self.author = ""
        self.keywords = []
        self.section = ""
