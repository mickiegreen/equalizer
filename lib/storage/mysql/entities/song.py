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
import equalizer.config as app

class Song(Entity):
    """ song table entity """

    def __init__(self, song_id = 0, song_title = None, country = None, genre = None,
                 release_date = None, itunes_song_id = None, duration = None, **kwargs):
        super(Song, self).__init__(
            table=app.SONG_TABLE,
            primary_key=app.SONG_TABLE_PK,
            select_query=app.SONG_EXISTS_QUERY
        )
        self.song_id = song_id
        self.song_title = song_title
        self.duration = duration
        self.country = country
        self.genre = genre
        self.release_date = release_date
        self.itunes_song_id = itunes_song_id