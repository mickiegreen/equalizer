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


RELEVANT_ARTIST_SONGS = {
    'query' :
                'SELECT youtube_video_id, youtube_video_title '
                'from join_song_video_artist '
                'where artist_id in '
                '(select artist_id '
                'from join_song_artist '
                'where YEAR(CURDATE())-YEAR(release_date) <= 5 '    
                'and genre = "%s"'
                'group by artist_id) '
                'group by youtube_video_id '
                'limit 10 ',
    'mode'  : 'select',
    'default' : {"genre":parseGenre()}
}

SELECT_GENRE = {
    'query':
        'SELECT distinct(genre) as genre '
        'from song ',
    'mode' : 'select'
}

