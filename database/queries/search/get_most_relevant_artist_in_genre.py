'''
This is a query which selects top 10 music videos by the most 'relevant' artists in
specific genre.
We define relevant as the artists who released a song most recently.
The nested queries fetch those artists_id and returns 10 of their songs.
'''
MOST_RELEVANT_ARTISTS_GENRE_SONGS = {
    'query': '''
                SELECT DISTINCT youtube_video_id, youtube_video_title, video_id, (likes + comments + views) AS popularity
                FROM artist_song_video_view 
                WHERE artist_id IN (
                    SELECT artist_id 
                    FROM (
                        SELECT DISTINCT artist_id, COUNT(song_id) AS score, MIN(YEAR(CURDATE())-YEAR(release_date)) as `gap` 
                        FROM artist_song_view 
                        WHERE genre = "%s" 
                        GROUP BY artist_id
                        ORDER BY `gap` 
                    ) AS artists)
                GROUP BY youtube_video_id
                ORDER BY popularity DESC
                LIMIT 10 
             ''',
    'mode'  : 'select',
    'args' : ['genre']
}