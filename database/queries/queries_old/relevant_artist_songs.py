'''
This is a query which selects top 10 music videos by the most 'relevant' artists.
We decided a 'relevant' artist is an artist who released a song in the last 5 years.
The query select 10 music videos, who's artist has released a song in the last 5 years in a certain genre.
The genre is randomly chosen each time the query is executed.
'''
RELEVANT_ARTIST_SONGS = {
    'query': '''
               SELECT youtube_video_id, youtube_video_title 
               FROM artist_song_video_view 
               WHERE artist_id in 
               (SELECT artist_id 
               FROM(
               SELECT artist_id ,sum(song_id) as sum 
               FROM artist_song_view 
               WHERE YEAR(CURDATE())-YEAR(release_date) <= 5    
               AND genre = "%s" 
               GROUP BY artist_id
               HAVING sum > 250000) as artists)
               GROUP BY youtube_video_id 
               LIMIT 10 ''',
    'mode'  : 'select',
    'args' : ['genre']
}
