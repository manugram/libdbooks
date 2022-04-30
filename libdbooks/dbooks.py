# libdbooks - Copyright (c) 2022 Manuel Soto
# This software is distributed under the terms of the GNU General
# Public License
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from . import __version__

from urllib.parse import quote_plus
from urllib.request import urlopen, Request
import json


class DBooks(object):
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
                     'url': '',         <- Book page url
                },
            ]
        }
    Which is the current json structure of the api.
    """

    _BASE_URL = 'https://www.dbooks.org/api/'

    _REQ_HEADER = {
        "User-Agent":"libdbooks/0.2.0",
    }


    def __init__(self,/, search_term=None, book_id=None):
        self._search_term = search_term
        self._book_id = book_id
        self.status = None
        self.total = None
        self.books = None


    def get_version(self):
        return __version__


    def _req_construct(self, api_req: str):
        """
        Helper method to construct request object.
        """

        req = Request(''.join([self._BASE_URL, api_req]),
                      headers=self._REQ_HEADER)

        return req


    def get_recents_books(self):
        """
        Get recent uploads.
        """

        with urlopen(self._req_construct('recent')) as res:
            recents = json.loads(res.read())
            if recents is not None:
                self.status = recents.get('status')
                self.total = recents.get('total')
                self.books = recents.get('books')

        return recents


    def search_book(self,/, sterm: str) -> dict:
        """
        Search books by search term "sterm".
        """

        if self._search_term is not None:
            if sterm is None:
                sterm = self._search_term

        parsed_sterm = quote_plus(sterm)

        api_str = ''.join(['search/', '{}'.format(parsed_sterm)])
        req = self._req_construct(api_str)

        with urlopen(req) as res:
            founds = json.loads(res.read())
            if founds is not None:
                self.status = founds.get('status')
                self.total = founds.get('total')
                self.books = founds.get('books')

        return founds


    def get_book_details(self,/, book_id: str) -> dict:
        """
        Show book details by id.
        """

        if self._book_id is not None and book_id is None:
            book_id = self._book_id

        api_str = ''.join(['book/','{}'.format(book_id)])
        req = self._req_construct(api_str)

        with urlopen(req) as res:
            details = json.loads(res.read())

        return details
    
    
