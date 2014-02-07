#!/usr/bin/python

import unittest

# Populate isbn dict
isbns = [line.strip() for line in open('isbn_samples.txt').readlines() if line.strip()]

class IsbnTests(unittest.TestCase):

    def testPrintIsbns(self):
	for isbn in isbns:
          print isbn
        self.assertTrue(True)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
