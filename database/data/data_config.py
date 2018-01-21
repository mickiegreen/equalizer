#******************************#
#                              #
#              API             #
#                              #
#******************************#

from equalizer.lib.parsers import ItunesDatetimeParser, \
    DurationParser, IntegerParser, IdentityParser

# youtube
YOUTUBE_TOKEN = 'AIzaSyATGzqdcCvkr_lV4ocVhagTKDCO6Ng-ods'
YOUTUBE_OUTPUT_FOLDER = '/home/michael/Projects/equalizer/venv/equalizer/resources/youtube'
YOUTUBE_UPDATE_ENTRIES = True
YOUTUBE_VIDEO_LIMIT = 2
YOUTUBE_ITUNES_PARSE = {}

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