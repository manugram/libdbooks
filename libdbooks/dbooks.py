import sys
import requests
from pprint import pformat


PYTHON_MIN_VERSION = (3,8)
PYTHON_VERSION = sys.version_info[0:2]

if PYTHON_VERSION < PYTHON_MIN_VERSION:
    sys.exit(5)

class DBooks:
    """
    Class to interface the dbooks.org api.

    Each method return a dictionary structure like following:
        {
            'status': 'ok',
            'total': 'X', <- Where X is the number of books found.
            'books': [ <- List of dictionaries.
                {
                     'id': 'XXXXX',     <- Books id.
                     'title': '',       <- Book title string
                     'subtitle': '',    <- Subtitle string
                     'authors': '',     <- Comma separated authors name
                     'image': '',       <- Book cover url
                     'url': ''          <- Book page url
                },
            ]
        }
    What is the current json structure of the api.
    """

    _URL = 'https://www.dbooks.org/api/'


    def __init__(self, book=None):
        self.book = book


    def recent_books(self,*, indent=None, depth=None, sort=False):
        """
        Query for recent uploaded books.

        With any of indent, depth and sort options, return a formtted string
         to pretty printing, but losing any dictionary object advantages.
        """

        with requests.get(''.join([self._URL, 'recent'])) as r:
                if indent is not None:
                    return pformat(r.json(), indent=indent, depth=depth, sort_dicts=sort)
                else:
                    return r.json()


    def search_book(self, search_term: str,/, indent=None, depth=None, sort=False):
        """
        Search a book by search_term string, returning a python dictionary.

        With any of indent, depth and sort options, return a formtted string
         to pretty printing, but losing any dictionary object advantages.
        """

        with requests.get(''.join([self._URL, f'search/{search_term}'])) as s:
            if indent is not None:
                return pformat(s.json(), indent=indent, depth=depth, sort_dicts=sort)
            else:
                return s.json()


    def book_details(self, book_id: str,/, indent=None, depth=None, sort=False):
        """
        Query for book details passing the book id param.

        With any of indent, depth and sort options, return a formtted string
         to pretty printing, but losing any dictionary object advantages.
        """

        if book_id is not None:
            with requests.get(''.join([self._URL, f'book/{book_id}'])) as d:
                if indent is not None:
                    return pformat(d.json(), indent=indent, depth=depth, sort_dicts=sort)
                else:
                    return d.json()
        else:
            return dict()




if __name__ == '__main__':
    pass