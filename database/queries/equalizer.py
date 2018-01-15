from equalizer.lib.api.mysql import MysqlApi
from equalizer.lib.storage.mysql import MySqlEngine

import equalizer.config as app
import random

'''
parseGenre() & parseCountry() are function which returns a random genre/country from the DB.
Each function creates an array of all genres/countries in DB using a query which returns all genres/countries from DB.
Then randomly chooses 1 of them and return it.
'''
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

'''
This query select top 10 music videos based on a score we made using the following parameters:
1.views
2.comments
3.likes
4.genre
5.country
This is the user custom playlist making query, the user set a value to each parameter by it's importance. 
The values are between 1 to 10, and the score is constructed in the following way:
score of a row = row_views*user_views_value + row_likes*user_likes_value ...
Then pick 10 rows who has the highest score (order it by score and limit select to only 10 rows).
'''

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

# a query we use to generate a random genre for the 'equalizer' query.
SELECT_GENRE = {
    'query':
        'SELECT distinct(genre) as genre '
        'from song ',
    'mode' : 'select'
}

# a query we use to generate a random country for the 'equalizer' query.
SELECT_COUNTRY = {
    'query':
        'SELECT distinct(country) as country '
        'from song ',
    'mode' : 'select'
}
