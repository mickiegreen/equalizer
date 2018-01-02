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

try:
    from .config_local import *
except:
    pass



