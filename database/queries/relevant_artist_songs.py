from equalizer.lib.api.mysql import MysqlApi
from equalizer.lib.storage.mysql import MySqlEngine

import equalizer.config as app
import random

'''
parseGenre() is a function which returns a random genre from the DB genres.
The function creates an array of all genres in DB using a query which returns all genres.
Then randomly chooses 1 of them and return it.
'''
def parseGenre () :
    engine = MySqlEngine(**app.MYSQL_INFO)
    mysql_api = MysqlApi(engine)
    response = mysql_api.execute(**SELECT_GENRE)
    genres = [item['genre'] for item in response]
    random.shuffle(genres)
    return genres[0]

'''
This is a query which selects top 10 music videos by the most 'relevant' artists.
We decided a 'relevant' artist is an artist who released a song in the last 5 years.
The query select 10 music videos, who's artist has released a song in the last 5 years in a certain genre.
The genre is randomly chosen each time the query is executed. 
'''
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

# a query we use to generate a random genre for the 'relevant artist' query.
SELECT_GENRE = {
    'query':
        'SELECT distinct(genre) as genre '
        'from song ',
    'mode' : 'select'
}

