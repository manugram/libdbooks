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
        self.assertIsInstance(self.dbooks, DBooks, 'Class instantiated.')
        self.assertIsNotNone(self.dbooks.books, 'books is not None.')
        self.assertIsInstance(self.recents, dict, 'Recents correctly obtain.')


    def test_search(self):
        self.assertIsInstance(self.search, dict, 'Search result store correctly.')


    def test_details(self):
        self.assertIsInstance(self.details, dict, 'Book detail correctly obtain.')


    def test_version(self):
        self.assertIsNotNone(self.version)


if __name__ == '__main__':
    unittest.main()

