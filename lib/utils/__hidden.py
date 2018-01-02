import os
import json
import datetime
import random
import string

from lib.api.youtube import add_token, search, get
from lib.storage.mysql.entities import Artist, ArtistSong, ArtistSongVideo, \
    Song, YoutubeVideo

from lib.storage import MySqlEngine

import config as app

add_token(app.YOUTUBE_TOKEN)

# itunes-youtube data intersection
ITUNES_TO_YOUTUBE = ['artist_name', 'song_title']

sql_parser = lambda x : '"' + str(x) + '"' if str(x).count('\'') > 0 else "'" + str(x) +"'"
id_parser = lambda x : int(x)
time_parser = lambda x : "'" + str(datetime.datetime.fromtimestamp(x/1000.0).time()) + "'"
itunes_date_parser = lambda x : "'" + str(datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ')) + "'"

ITUNES_TO_MYSQL = {
    'artistName'            : 'artist_name',
    'artistId'              : 'itunes_artist_id',
    'primaryGenreName'      : 'genre',
    'country'               : 'country',
    'releaseDate'           : 'release_date',
    'trackId'               : 'itunes_song_id',
    'trackName'             : 'song_title',
    'trackTimeMillis'       : 'duration',
    'duration'              : 'release_date',
}

RECORD_TO_MYSQL = {
    'views'                     : {'key' : 'views',                 'val' : id_parser },
    'likes'                     : {'key' : 'likes',                 'val' : id_parser },
    'comments'                  : {'key' : 'comments',              'val' : id_parser },
    'dislikes'                  : {'key' : 'dislikes',              'val' : id_parser },
    'youtube_video_title'       : {'key' : 'youtube_video_title',   'val' : sql_parser },
    'favorites'                 : {'key' : 'favorites',             'val' : id_parser },
    'youtube_video_id'          : {'key' : 'favorites',             'val' : sql_parser },
    'artist_name'               : {'key' : 'artist_name',           'val' : sql_parser },
    'itunes_artist_id'          : {'key' : 'itunes_artist_id',      'val' : sql_parser },
    'genre'                     : {'key' : 'genre',                 'val' : sql_parser },
    'country'                   : {'key' : 'country',               'val' : sql_parser },
    'release_date'              : {'key' : 'release_date',          'val' : itunes_date_parser },
    'itunes_song_id'            : {'key' : 'itunes_song_id',        'val' : sql_parser },
    'song_title'                : {'key' : 'song_title',            'val' : sql_parser },
    'duration'                  : {'key' : 'duration',              'val' : time_parser },
}

ITUNES_TRACKS = []
ITUNES_ARTISTS = []
ITUNES_TRACKS_ARTISTS = []
ITUNES_TRACKS_ARTISTS_VIDEOS = []

ITUNES_OUTPUT_FOLDER = '/home/michael/Projects/equalizer/venv/equalizer/resources/itunes'
YOUTUBE_OUTPUT_FOLDER = '/home/michael/Projects/equalizer/venv/equalizer/resources/youtube'
YOUTUBE_OUTPUT_CHUNK_SIZE = 100
YOUTUBE_NAME_LENGTH = 20

def generate_random_str(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def get_records_name():
    return str(datetime.datetime.now()) + generate_random_str(YOUTUBE_NAME_LENGTH) + '.txt'

def itunes_record_to_mysql(record):
    rmysql = [{v : record[k] for k,v in ITUNES_TO_MYSQL.items() if record.get(k, None) != None}]
    if record.get('collectionArtistId', None)!= None \
        and record.get('collectionArtistId', None) != record.get("artistId") :
        rmysql2 = rmysql[0].copy()
        rmysql2['artist_id'] = record.get('collectionArtistId')
        rmysql2['artist_name'] = record.get('collectionArtistName')
        rmysql.append(rmysql2)

    return rmysql

def load_itunes_results(limit = 20000):
    """ fetch all itunes data from local folder """
    itunes = []

    for dirName, subdirList, fileList in os.walk(ITUNES_OUTPUT_FOLDER):

        for _file in fileList:
            if not _file.endswith(".txt") and not _file.endswith(".text"): continue

            with open(ITUNES_OUTPUT_FOLDER + os.sep + _file, 'r') as _f:

                # merge all results to one list
                itunes.extend(json.load(_f)['results'])

            if len(itunes) >= limit:
                break

    return [ rmysql for record in itunes for rmysql in itunes_record_to_mysql(record) ]

def itunes_keywords(result):
    # fetch keywords from itunes record
    keywords = []

    for key in ITUNES_TO_YOUTUBE:
        keywords.extend(str(result.get(key,'')).split(' '))

    return keywords

def itunes_to_youtube(itunes):
    results = []

    # for each itunes track in data
    for i, record in enumerate(itunes):

        # get record keywords
        keywords = itunes_keywords(record)

        # search for videos with same keywords
        videos = search(keywords, **app.YOUTUBE_VIDEO_KEYS)

        for video in videos:
            # make copy of record to extend
            rcopy = record.copy()

            # get info for each video found
            res = get(video['youtube_video_id'], **app.YOUTUBE_VIDEO_KEYS)
            rcopy.update(res)
            rcopy.update(video)

            for k,v in rcopy.items():
                parser = RECORD_TO_MYSQL.get(k, None) if RECORD_TO_MYSQL.get(k, None) else ITUNES_TO_MYSQL.get(k, None)

                if parser != None:
                    rcopy[k] = parser.get('val',lambda x : x)(v)

            # init non exists id's as zero
            rcopy['song_id'] = id_parser(0)
            rcopy['artist_id'] = id_parser(0)
            rcopy['video_id'] = id_parser(0)
            rcopy['artist_song_id'] = id_parser(0)
            rcopy['artist_song_video_id'] = id_parser(0)

            # add video to results
            results.append(rcopy)

        if len(results) >= YOUTUBE_OUTPUT_CHUNK_SIZE or i == len(itunes) - 1:
            filename = YOUTUBE_OUTPUT_FOLDER + os.sep + get_records_name()

            while os._exists(filename):
                filename = YOUTUBE_OUTPUT_FOLDER + os.sep + get_records_name()

            with open(filename, 'w') as _file:
                json.dump(results, _file)

            results = []

def load_full_records(limit = 20000):
    """ fetch all youtube data from local folder """
    youtube = []

    for dirName, subdirList, fileList in os.walk(YOUTUBE_OUTPUT_FOLDER):

        for _file in fileList:
            if not _file.endswith(".txt"): continue

            with open(YOUTUBE_OUTPUT_FOLDER + os.sep + _file, 'r') as _f:

                # merge all results to one list
                youtube.extend(json.load(_f))

            if len(youtube) >= limit:
                break

    return youtube

def records_to_mysql(data):

    engine = MySqlEngine(**app.MYSQL_INFO)

    for record in data:
        song = Song(**record)
        artist = Artist(**record)
        youtube_video = YoutubeVideo(**record)

        song_id = engine.update_if_exists_else_add(song)
        artist_id = engine.update_if_exists_else_add(artist)
        video_id = engine.update_if_exists_else_add(youtube_video)

        record['song_id'], record['artist_id'], record['video_id'] = song_id, artist_id, video_id
        artist_song = ArtistSong(**record)
        record['artist_song_id'] = engine.update_if_exists_else_add(artist_song)
        artist_song_video = ArtistSongVideo(**record)
        artist_song_video_id = engine.update_if_exists_else_add(artist_song_video)

def load_config(config):
    pass