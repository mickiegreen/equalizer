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

from song import Song
from artist_song import ArtistSong
from artist import Artist

from equalizer.lib.storage.mysql.attributes import IntegerAttribute, \
    DatetimeAttribute, TimedeltaAttribute, VarcharAttribute

from equalizer_view_entity import EqualizerViewEntity as Entity
import structure_config as app

# TODO handle as a view not regular entity
class JoinSongArtist(Entity):
    """ Join song video artist view entity """
    def __init__(self, song_id = 0, song_title = None, itunes_song_id = None,
                 artist_id = 0, artist_name = None, itunes_artist_id = None,
                 country = None, genre = None, duration = None, release_date = None,
                 **kwargs):
        super(JoinSongArtist, self).__init__(
            view = app.JOIN_SONG_ARTIST_VIEW,
            primary_key = app.JOIN_SONG_ARTIST_VIEW_PK,
            select_query = app.JOIN_SONG_ARTIST_EXISTS_QUERY,
            tables_entities = app.JOIN_SONG_ARTIST_ENTITIES
        )

        self.song_id = IntegerAttribute('song_id', song_id)
        self.song_title = VarcharAttribute('song_title', song_title)
        self.itunes_song_id = VarcharAttribute('itunes_song_id', itunes_song_id)
        self.artist_id = IntegerAttribute('artist_id', artist_id)
        self.artist_name = VarcharAttribute('artist_name', artist_name)
        self.itunes_artist_id = VarcharAttribute('itunes_artist_id', itunes_artist_id)
        self.country = VarcharAttribute('country', country)
        self.duration = TimedeltaAttribute('duration', duration)
        self.genre = VarcharAttribute('genre', genre)
        self.release_date = DatetimeAttribute('release_date', release_date)

    @overrides
    def insert_query(self):
        """ execute insert query, must have engine set """
        if not hasattr(self, 'engine'):
            raise ArithmeticError("view must have engine set before executing insert_query")

        engine = self.engine

        data = self.dict()

        # creating new entities and adding each
        song = Song(**data)
        artist = Artist(**data)

        # adding to storage
        song_id = engine.update_if_exists_else_add(song)
        artist_id = engine.update_if_exists_else_add(artist)

        if -1 in [song_id, artist_id]:
            raise RuntimeError("Some entries weren't added to database")

        # connecting through joinable relation
        data['song_id'], data['artist_id'] = song_id, artist_id
        artist_song = ArtistSong(**data)
        artist_song_id = data['artist_song_id'] = engine.update_if_exists_else_add(artist_song)

        # error if not added
        if -1 in [artist_song_id]:
            raise RuntimeError("Some entries weren't added to database")

        return data

    @overrides
    def updatable(self):
        """ view is updatable """
        return True


