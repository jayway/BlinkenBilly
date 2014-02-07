import os
import unittest
import bookinfo.isbn as isbn

# Test data is located in file
script_dir = os.path.dirname(__file__)
rel_path = "isbn_samples.txt"
isbn_data_path = os.path.join(script_dir, rel_path)

# Populate isbn dict
isbns = [line.strip() for line in open(isbn_data_path).readlines() if line.strip()]

class SimplisticTest(unittest.TestCase):

    def test_create_isbn(self):
        book = isbn.Isbn("9780970601971")
        self.assertEquals(book.isbn, "9780970601971")

    def test_get_title(self):
        book = isbn.Isbn("9780970601971")
        self.assertEquals(book.title, "Show Me the Numbers: Designing Tables and Graphs to Enlighten")

if __name__ == '__main__':
    unittest.main()
