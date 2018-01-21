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

from equalizer.lib.storage.mysql import MySqlEngine
from equalizer.database.structure import \
    JoinSongArtist, ArtistSongVideo, Artist, ArtistSong, \
    Song, JoinSongVideoArtist, JoinSongArtistNoVideo, YoutubeVideo

from database.data import ItunesDataHandler
from database.data import YoutubeDataHandler

from equalizer.database.data import data_config as app
from equalizer.config import MYSQL_INFO

def get_storage_engine():
    """
    :return MysqlEngine object adapter to handle mysql data:
    """
    return MySqlEngine(**MYSQL_INFO)

def get_more_youtube_data():
    """
    getting more videos from youtube
    """
    engine = get_storage_engine()

    youtube_keys = app.YOUTUBE_TO_MYSQL

    youtube_handler = YoutubeDataHandler(
        engine=engine,
        token=app.YOUTUBE_TOKEN,
        youtube_keys=youtube_keys
    )

    youtube_handler.get_more_data(
        output_dir=app.YOUTUBE_OUTPUT_FOLDER,
        limit=app.YOUTUBE_VIDEO_LIMIT,
        itunes_keys=app.ITUNES_TO_MYSQL,
        update=app.YOUTUBE_UPDATE_ENTRIES
    )

def remove_all_data():
    """ truncate database """

    # TODO - fix not removing
    engine = get_storage_engine()

    tables = [
        Artist, ArtistSong, ArtistSongVideo, YoutubeVideo,
        Song, JoinSongArtist, JoinSongArtistNoVideo, JoinSongVideoArtist
    ]

    for table in tables:
        # getting all data
        data = engine.fetch_all_like_entry(table())

        # removing each entry
        for row in data:
            engine.remove_safe(row)

def update_existing_data():
    """
    update storage data such as likes, comments. etc.
    """
    engine = get_storage_engine()

    youtube_keys = app.YOUTUBE_TO_MYSQL

    youtube_handler = YoutubeDataHandler(
        engine=engine,
        token=app.YOUTUBE_TOKEN,
        youtube_keys=youtube_keys
    )

    youtube_handler.update_all()

def complete_existing_song_data():
    """
    add video to each song data with no youtube video
    """
    engine = get_storage_engine()

    youtube_keys = app.YOUTUBE_TO_MYSQL

    youtube_handler = YoutubeDataHandler(
        engine=engine,
        token=app.YOUTUBE_TOKEN,
        youtube_keys=youtube_keys,
        search_keys=app.YOUTUBE_ITUNES_SEARCH_KEYWORDS
    )

    youtube_handler.complete_all_storage_data(
        output_dir = app.YOUTUBE_OUTPUT_FOLDER,
        limit = app.YOUTUBE_VIDEO_LIMIT,
        itunes_keys=app.ITUNES_TO_MYSQL,
        update = app.YOUTUBE_UPDATE_ENTRIES
    )

def init_itunes_data():
    """
    put all data from itunes in storage
    """
    engine = get_storage_engine()

    itunes_keys = app.ITUNES_TO_MYSQL
    additional_entries = app.ITUNES_ADDITIONAL_ENTRIES_TO_MYSQL

    itunes_handler = ItunesDataHandler(
        engine = engine,
        itunes_keys = itunes_keys,
        additional_entries = additional_entries,
    )

    itunes_handler.add_from_local_folder(
        app.ITUNES_OUTPUT_FOLDER,
        update = app.ITUNES_UPDATE_ENTRIES,
        limit = app.ITUNES_LIMIT_NUMBER_OF_ENTRIES
    )

def init_youtube_data():
    """
    put all data from youtube in storage
    """
    engine = get_storage_engine()

    youtube_keys = app.YOUTUBE_TO_MYSQL

    youtube_handler = YoutubeDataHandler(
        engine = engine,
        token = app.YOUTUBE_TOKEN,
        youtube_keys = youtube_keys
    )

    youtube_handler.add_from_local_folder(
        folder = app.YOUTUBE_OUTPUT_FOLDER,
        update = app.YOUTUBE_UPDATE_ENTRIES
    )

def init_search_data():
    """
    1. put all itunes data in db
    2. put all youtube data in db
    3. search for each song-artist with no video
       videos and dump results to Folder
    4. put all dumped youtube data to db
    """

    # 1. put all itunes data in db
    init_itunes_data()

    # 2. put all youtube data in db
    init_youtube_data()

    # 3. search for each song-artist with no video
    complete_existing_song_data()

    # 4. put all dumped youtube data to db
    init_youtube_data()

if __name__ == '__main__':

    # remove_all_data()
    # init_itunes_data()
    # update_existing_data()
    complete_existing_song_data()
    # get_more_youtube_data()


