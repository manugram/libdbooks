import unittest
from libdbooks import DBooks



class DBooksTestCase(unittest.TestCase):

    def setUp(self):
        self.dbooks = DBooks()
        self.recents = self.dbooks.get_recents_books()
        self.search = self.dbooks.search_book('vim')
        self.details = self.dbooks.get_book_details('1530051126')
        self.version = self.dbooks.get_version()


    def test_recents(self):
        self.assertIsInstance(self.dbooks, DBooks)
        self.assertIsNotNone(self.dbooks.books)
        self.assertIsInstance(self.recents, dict)


    def test_search(self):
        self.assertIsInstance(self.search, dict)


    def test_details(self):
        self.assertIsInstance(self.details, dict)


    def test_version(self):
        self.assertIsNotNone(self.version)


if __name__ == '__main__':
    unittest.main()

