from equalizer.lib.api.mysql import MysqlApi
from equalizer.lib.storage.mysql import MySqlEngine

import equalizer.config as app
import random

def parseGenre () :
    engine = MySqlEngine(**app.MYSQL_INFO)
    mysql_api = MysqlApi(engine)
    response = mysql_api.execute(**SELECT_GENRE)
    genres = [item['genre'] for item in response]
    random.shuffle(genres)
    return genres[0]

def parseCountry () :
    engine = MySqlEngine(**app.MYSQL_INFO)
    mysql_api = MysqlApi(engine)
    response = mysql_api.execute(**SELECT_COUNTRY)
    countries = [item['country'] for item in response]
    random.shuffle(countries)
    return countries[0]



EQUALIZER = {
    'query' :   'SELECT 0.1*views + 0.2*comments + 0.3*likes + 0.2*genre + 0.2*country AS score, youtube_video_title, youtube_video_id '
                'FROM join_song_vide_artist '
                'WHERE genre = "%s" '
                'AND country = "%s" '
                'ORDER BY score '
                'LIMIT 10',
    'mode'  : 'select',
    'default' :{"genre": parseGenre() , "country" : parseCountry()}
}


SELECT_GENRE = {
    'query':
        'SELECT distinct(genre) as genre '
        'from song ',
    'mode' : 'select'
}


SELECT_COUNTRY = {
    'query':
        'SELECT distinct(country) as country '
        'from song ',
    'mode' : 'select'
}
