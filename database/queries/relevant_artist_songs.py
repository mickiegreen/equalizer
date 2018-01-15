'''
This is a query which selects top 10 music videos by the most 'relevant' artists.
We decided a 'relevant' artist is an artist who released a song in the last 5 years.
The query select 10 music videos, who's artist has released a song in the last 5 years in a certain genre.
The genre is randomly chosen each time the query is executed.
'''
RELEVANT_ARTIST_SONGS = {
    'query': '''
               SELECT youtube_video_id, youtube_video_title 
               from join_song_video_artist 
               where artist_id in 
               (select artist_id 
               from join_song_artist 
               where YEAR(CURDATE())-YEAR(release_date) <= 5    
               and genre = "%s" 
               group by artist_id) 
               group by youtube_video_id 
               limit 10 ''',
    'mode'  : 'select',
    'args' : ['genre']
}

# a query we use to generate a random genre for the 'relevant artist' query.

SELECT_GENRE = {
    'query':
        'SELECT distinct(genre) as genre '
        'from song ',
    'mode' : 'select'
}

