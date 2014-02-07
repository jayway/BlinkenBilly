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

    def test_get_author(self):
        book = isbn.Isbn("9780970601971")
        self.assertEquals(book.authors, ["Stephen Few"])

    def test_get_author_no_hyperlink(self):
        book = isbn.Isbn("9781449360078")
        self.assertEquals(book.authors, ["Jamie Allen"])

    def test_get_authors(self):
        book = isbn.Isbn("9780988262591")
        self.assertEquals(book.authors, ["Gene Kim", "Kevin Behr", "George Spafford"])

    def test_get_authors_no_hyperlink(self):
        book = isbn.Isbn("9780321718334")
        self.assertEquals(book.authors, ["Nick Rozanski", "E\xc3in Woods"])

    def test_get_authors_some_hyperlinks(self):
        book = isbn.Isbn("9781449339197")
        self.assertEquals(book.authors, ["Jurg van Vliet", "Flavia Paganelli", "Jasper Geurtsen"])

if __name__ == '__main__':
    unittest.main()
