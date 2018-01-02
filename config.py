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

#******************************#
#                              #
#              API             #
#                              #
#******************************#

# youtube
YOUTUBE_FIELDS = []

YOUTUBE_TOKEN = 'AIzaSyATGzqdcCvkr_lV4ocVhagTKDCO6Ng-ods'

YOUTUBE_VIDEO_KEYS = {
    "viewCount"         : "views",
    "likeCount"         : "likes",
    "dislikeCount"      : "dislikes",
    "favoriteCount"     : "favorites",
    "commentCount"      : "comments",
    "title"             : "youtube_video_title"
}

# itunes
ITUNES_CATALOG_URL = ''
ITUNES_FIELDS = []
ITUNES_LIMIT = 200
ITUNES_OVERRIDE = True

#******************************#
#                              #
#             MySQL            #
#                              #
#******************************#
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_SCHEMA = ''
MYSQL_USER = ''
MYSQL_PASSWORD = ''

MYSQL_INFO = {
    'host'          : MYSQL_HOST,
    'port'          : MYSQL_PORT,
    'schema'        : MYSQL_SCHEMA,
    'user'          : MYSQL_USER,
    'password'      : MYSQL_PASSWORD
}

#******************************#
#                              #
#            Queries           #
#                              #
#******************************#

SONG_TABLE = "song"
SONG_TABLE_PK = "song_id"
SONG_EXISTS_QUERY = {
    "query" : "SELECT * FROM song WHERE itunes_song_id=%s",
    "keys"  : ["itunes_song_id"]
}

ARTIST_TABLE = "artist"
ARTIST_TABLE_PK = "artist_id"
ARTIST_EXISTS_QUERY = {
    "query" : "SELECT * FROM artist WHERE itunes_artist_id=%s",
    "keys"  : ["itunes_artist_id"]
}

ARTIST_SONG_TABLE = "artist_song"
ARTIST_SONG_TABLE_PK = "artist_song_id"
ARTIST_SONG_EXISTS_QUERY = {
    "query" : "SELECT * FROM artist_song WHERE artist_id=%s AND song_id=%s",
    "keys"  : ["artist_id", "song_id"]
}

ARTIST_SONG_VIDEO_TABLE = "artist_song_video"
ARTIST_SONG_VIDEO_TABLE_PK = "artist_song_video_id"
ARTIST_SONG_VIDEO_EXISTS_QUERY = {
    "query" : "SELECT * FROM artist_song_video WHERE artist_song_id=%s AND video_id=%s",
    "keys"  : ["artist_song_id", "video_id"]
}

YOUTUBE_VIDEO_TABLE = "youtube_video"
YOUTUBE_VIDEO_TABLE_PK = "video_id"
YOUTUBE_VIDEO_EXISTS_QUERY = {
    "query" : "SELECT * FROM youtube_video WHERE youtube_video_id=%s",
    "keys"  : ["youtube_video_id"]
}

USER_TABLE = "user"
USER_TABLE_PK = "user_id"
USER_EXISTS_QUERY = {
    "query" : "SELECT * FROM user WHERE email=%s",
    "keys"  : ["email"]
}

USER_SEARCH_HISTORY_TABLE = "user_search_history"
USER_SEARCH_HISTORY_TABLE_PK = "history_id"
USER_SEARCH_HISTORY_EXISTS_QUERY = {
    "query" : "SELECT * FROM user_search_history WHERE history_id=%s",
    "keys"  : ["history_id"]
}

INSERT_QUERY = "INSERT INTO %s (%s) VALUES (%s)"
UPDATE_QUERY = "UPDATE %s SET %s WHERE %s=%d"
REMOVE_QUERY = "DELETE FROM %s WHERE %s=%s"
TRUNCATE_QUERY = "DELETE FROM %s"

#******************************#
#                              #
#         API to MySQL         #
#                              #
#******************************#

YOUTUBE_TO_MYSQL = {
    'videoId'   : 'video_id',
    'title'     : 'name',
    'likes'     : 'likes'
}

#******************************#
#                              #
#           SSH Server         #
#                              #
#******************************#
SSH_HOST = 'localhost'
SSH_PORT = '22'
SSH_USER = ''
SSH_PASSWORD = ''

#******************************#
#                              #
#           LOGGING            #
#                              #
#******************************#
import logging

LOG_FILE_NAME = 'equalizer.log'
LOGGER_CONFIG = True
LOGGING_LEVEL = logging.DEBUG

def __set_logger():
    import sys
    logging.basicConfig(filename=LOG_FILE_NAME,
             filemode='a',
             format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
             datefmt='%H:%M:%S',
             level=LOGGING_LEVEL)
    logger = logging.getLogger()
    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)

if LOGGER_CONFIG:
    __set_logger()

LOGGER = logging.getLogger()

try:
    from config_local import *
except:
    pass



