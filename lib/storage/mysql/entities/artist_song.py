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

from overrides import overrides

from ..abstract_entity import AbstractEntity as Entity
import config as app
from ..attributes import PrimaryKey, IntegerAttribute

class ArtistSong(Entity):
    """ artist_song table entry """
    def __init__(self, artist_song_id = 0, artist_id = None,
                 song_id = None, **kwargs):
        super(ArtistSong, self).__init__(
            table=app.ARTIST_SONG_TABLE,
            primary_key=app.ARTIST_SONG_TABLE_PK,
            select_query=app.ARTIST_SONG_EXISTS_QUERY,
            remove_all_references = app.ARTIST_REMOVE_ALL_REFERENCES_QUERY
        )
        self.artist_song_id = PrimaryKey('artist_song_id', artist_song_id)
        self.artist_id = IntegerAttribute('artist_id', artist_id)
        self.song_id = IntegerAttribute('song_id', song_id)
