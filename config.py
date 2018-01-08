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

from equalizer.lib.data.parsers import ItunesDatetimeParser, \
    DurationParser, IntegerParser, IdentityParser

# youtube
YOUTUBE_TOKEN = 'AIzaSyATGzqdcCvkr_lV4ocVhagTKDCO6Ng-ods'
YOUTUBE_OUTPUT_FOLDER = '/home/michael/Projects/equalizer/venv/equalizer/resources/youtube'
YOUTUBE_UPDATE_ENTRIES = True
YOUTUBE_VIDEO_LIMIT = 2
YOUTUBE_ITUNES_PARSE = {
    # 'release_date'  : DatetimeParser,
    # 'duration'      : DatetimeParser
}

YOUTUBE_ITUNES_SEARCH_KEYWORDS = ['artist_name', 'song_title']
YOUTUBE_SEARCH_REGEX = ['(',')','{','}','<''>', '\"','\'', '\[.*?\]','\n','=','+']

YOUTUBE_TO_MYSQL = {
    'viewCount'                     : {
        'key'       : 'views',
        'parser'    : IntegerParser
    },

    'likeCount' : {
        'key'       : 'likes',
        'parser'    : IntegerParser
    },

    'commentCount' : {
        'key'       : 'comments',
        'parser'    : IntegerParser
    },

    'dislikeCount' : {
        'key'       : 'dislikes',
        'parser'    : IntegerParser
    },

    'title' : {
        'key'       : 'youtube_video_title',
        'parser'    : IdentityParser
    },

    'favoriteCount' : {
        'key'       : 'favorites',
        'parser'    : IntegerParser
    },

    'videoId' : {
        'key'       : 'youtube_video_id',
        'parser'    : IdentityParser
    },
}

# itunes
ITUNES_CATALOG_URL = ''
ITUNES_FIELDS = []
ITUNES_LIMIT = 200
ITUNES_OVERRIDE = True
ITUNES_OUTPUT_FOLDER = '/home/michael/Projects/equalizer/venv/equalizer/resources/itunes'
ITUNES_UPDATE_ENTRIES = True
ITUNES_LIMIT_NUMBER_OF_ENTRIES = 30000

# converting itunes keys to mysql
ITUNES_TO_MYSQL = {
    'artistName' : {
        'key'       : 'artist_name',
        'parser'    : IdentityParser
    },

    'artistId' : {
        'key'       : 'itunes_artist_id',
        'parser'    : IdentityParser
    },

    'primaryGenreName' : {
        'key'       : 'genre',
        'parser'    : IdentityParser
    },

    'country' : {
        'key'       : 'country',
        'parser'    : IdentityParser
    },

    'releaseDate' : {
        'key'       : 'release_date',
        'parser'    : ItunesDatetimeParser
    },

    'trackId'            : {
        'key'       : 'itunes_song_id',
        'parser'    : IdentityParser
    },

    'trackName' : {
        'key'       : 'song_title',
        'parser'    : IdentityParser
    },

    'trackTimeMillis' : {
        'key'       : 'duration',
        'parser'    : DurationParser
    },
}

ITUNES_ADDITIONAL_ENTRIES_TO_MYSQL = [{
    'collectionArtistName' : {
        'key'       : 'artist_name',
        'parser'    : IdentityParser
    },

    'collectionArtistId' : {
        'key'       : 'itunes_artist_id',
        'parser'    : IdentityParser
    },
}]

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

SONG_REMOVE_ALL_REFERENCES_QUERY = {
    "query" : \
        "DELETE s, sa, sav " + \
        "FROM song s " + \
        "INNER JOIN artist_song AS sa " + \
        "INNER JOIN artist_song_video AS sav " + \
        "WHERE s.song_id=sa.song_id " + \
        "AND sa.artist_song_id=sav.artist_song_id " + \
        "AND s.song_id=%s",
    "keys"  : ["song_id"]
}

ARTIST_TABLE = "artist"
ARTIST_TABLE_PK = "artist_id"
ARTIST_EXISTS_QUERY = {
    "query" : "SELECT * FROM artist WHERE itunes_artist_id=%s",
    "keys"  : ["itunes_artist_id"]
}
ARTIST_REMOVE_ALL_REFERENCES_QUERY = {
    "query" : \
        "DELETE a, sa, sav " + \
        "FROM artist a " + \
        "INNER JOIN artist_song AS sa " + \
        "INNER JOIN artist_song_video AS sav " + \
        "WHERE a.artist_id=sa.artist_id " + \
        "AND sa.artist_song_id=sav.artist_song_id " + \
        "AND a.artist_id=%s ",
    "keys"  : ["artist_id"]
}

ARTIST_SONG_TABLE = "artist_song"
ARTIST_SONG_TABLE_PK = "artist_song_id"
ARTIST_SONG_EXISTS_QUERY = {
    "query" : "SELECT * FROM artist_song WHERE artist_id=%s AND song_id=%s",
    "keys"  : ["artist_id", "song_id"]
}
ARTIST_SONG_REMOVE_ALL_REFERENCES_QUERY = {
    "query" : \
        "DELETE sa, sav " + \
        "FROM artist_song sa " + \
        "INNER JOIN artist_song_video AS sav " + \
        "WHERE sa.artist_song_id=sav.artist_song_id " + \
        "AND sa.artist_song_id=%s ",
    "keys"  : ["artist_song_id"]
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
YOUTUBE_VIDEO_REMOVE_ALL_REFERENCES_QUERY = {
    "query" : \
        "DELETE v, sav " + \
        "FROM youtube_video v " + \
        "INNER JOIN artist_song_video AS sav " + \
        "WHERE v.video_id=sav.video_id AND v.video_id=%s",
    "keys"  : ["video_id"]
}

USER_TABLE = "user"
USER_TABLE_PK = "user_id"
USER_EXISTS_QUERY = {
    "query" : "SELECT * FROM user WHERE email=%s",
    "keys"  : ["email"]
}

USER_REMOVE_ALL_REFERENCES_QUERY = {
    "query" : \
        "DELETE u, uh " + \
        "FROM user u " + \
        "INNER JOIN user_search_history AS uh " + \
        "WHERE u.user_id=uh.user_id AND u.user_id=%s",
    "keys"  : ["user_id"]
}

USER_SEARCH_HISTORY_TABLE = "user_search_history"
USER_SEARCH_HISTORY_TABLE_PK = "history_id"
USER_SEARCH_HISTORY_EXISTS_QUERY = {
    "query" : "SELECT * FROM user_search_history WHERE history_id=%s",
    "keys"  : ["history_id"]
}

JOIN_SONG_VIDEO_ARTIST_VIEW = "join_song_video_artist"
JOIN_SONG_VIDEO_ARTIST_VIEW_PK = ["video_id", "artist_id", "song_id"]
JOIN_SONG_VIDEO_ARTIST_EXISTS_QUERY = {
    "query" : "SELECT * FROM join_song_video_artist WHERE youtube_video_id=%s " + \
              "AND itunes_artist_id=%s AND itunes_song_id=%s",
    "keys"  : ["youtube_video_id", "itunes_artist_id", "itunes_song_id"]
}
JOIN_SONG_VIDEO_ARTIST_ENTITIES = [SONG_TABLE, ARTIST_TABLE, ARTIST_SONG_TABLE,
                             ARTIST_SONG_VIDEO_TABLE, YOUTUBE_VIDEO_TABLE]

JOIN_SONG_ARTIST_VIEW = "join_song_artist"
JOIN_SONG_ARTIST_VIEW_PK = ["artist_id", "song_id"]
JOIN_SONG_ARTIST_EXISTS_QUERY = {
    "query" : "SELECT * FROM join_song_artist WHERE itunes_artist_id=%s AND itunes_song_id=%s",
    "keys"  : ["itunes_artist_id", "itunes_song_id"]
}
JOIN_SONG_ARTIST_ENTITIES = [SONG_TABLE, ARTIST_TABLE, ARTIST_SONG_TABLE]


JOIN_SONG_ARTIST_NO_VIDEO_VIEW = "join_song_artist_no_videos"
JOIN_SONG_ARTIST_NO_VIDEO_VIEW_PK = ["itunes_artist_id", "itunes_song_id"]
JOIN_SONG_ARTIST_NO_VIDEO_EXISTS_QUERY = {
    "query" : "SELECT * FROM join_song_artist_no_video WHERE itunes_artist_id=%s AND itunes_song_id=%s",
    "keys"  : ["itunes_artist_id", "itunes_song_id"]
}

JOIN_SONG_ARTIST_NO_VIDEO_ENTITIES = JOIN_SONG_ARTIST_ENTITIES

INSERT_QUERY = "INSERT INTO %s (%s) VALUES (%s)"
UPDATE_QUERY = "UPDATE %s SET %s WHERE %s=%s"
REMOVE_QUERY = "DELETE FROM %s WHERE %s=%s"
TRUNCATE_QUERY = "DELETE FROM %s"
SELECT_ALL_QUERY = "SELECT * FROM %s"

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

LOG_FILE_NAME = 'equalizer.log'
LOGGER_CONFIG = False
LOGGING_LEVEL = 'INFO'

__loggers = {}

def __set_logger():
    # TODO put logging configurations in __hidden
    import sys
    import logging
    from logging import handlers
    formatter = logging.Formatter(
        '\n'
        'TIME    :: [%(asctime)s,%(msecs)d]\n'
        'FILE    :: [<%(filename)s> at line <%(lineno)d>]\n'
        'LEVEL   :: [%(levelname)s]\n'
        'MESSAGE :: %(message)s'
    )
    logging.basicConfig(filename=LOG_FILE_NAME,
             filemode='a',
             datefmt='%H:%M:%S',
             level=LOGGING_LEVEL)
    logger = logging.getLogger(LOG_FILE_NAME)
    if not logger.handlers:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        fh = handlers.RotatingFileHandler(LOG_FILE_NAME, maxBytes=(104857), backupCount=7)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    __loggers['logger'] = logging.getLogger(LOG_FILE_NAME)

if len(__loggers) == 0:
    __set_logger()

LOGGER = __loggers['logger']

try:
    from config_local import *
except:
    pass



