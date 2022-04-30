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

"""
A library that provides a Python 3 interface to the dbooks.org API.
"""

__author__ = "Manuel Soto <manugram.dev@gmail.com>"
__version__ = (0,2,0)


import sys

if sys.version_info[0] < 3:
    # For Python 2
    raise RuntimeError('No Python 2 suport right now.')
else:
    # For Python 3
    from .dbooks import DBooks
