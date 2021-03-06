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

from equalizer.lib.storage.mysql.attributes import PrimaryKey, IntegerAttribute

from equalizer_abstract_entity import EqualizerAbstractEntity as Entity
import structure_config as app

class ArtistSongVideo(Entity):
    """ artist_song_video table entity"""
    def __init__(self, artist_song_video_id = 0,
                 artist_song_id = 0, video_id = 0, **kwargs):
        super(ArtistSongVideo, self).__init__(
            table=app.ARTIST_SONG_VIDEO_TABLE,
            primary_key=app.ARTIST_SONG_VIDEO_TABLE_PK,
            select_query=app.ARTIST_SONG_VIDEO_EXISTS_QUERY,
        )
        self.artist_song_video_id = PrimaryKey('artist_song_video_id', artist_song_video_id)
        self.artist_song_id = IntegerAttribute('artist_song_id', artist_song_id)
        self.video_id = IntegerAttribute('video_id', video_id)
