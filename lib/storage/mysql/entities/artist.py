# -*- coding: utf-8 -*-

# Copyright (c) 2018 Michael Green
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from ..abstract_entity import AbstractEntity as Entity
from ..attributes import PrimaryKey, VarcharAttribute

import config as app

class Artist(Entity):
    """ Artist table entity """
    def __init__(self, artist_id = 0, artist_name = None, itunes_artist_id = None, **kwargs):
        super(Artist, self).__init__(
            table = app.ARTIST_TABLE,
            primary_key = app.ARTIST_TABLE_PK,
            select_query = app.ARTIST_EXISTS_QUERY,
            remove_all_references = app.ARTIST_REMOVE_ALL_REFERENCES_QUERY
        )
        self.artist_id = PrimaryKey('artist_id', artist_id)
        self.artist_name = VarcharAttribute('artist_name', artist_name)
        self.itunes_artist_id = VarcharAttribute('itunes_artist_id', itunes_artist_id)


