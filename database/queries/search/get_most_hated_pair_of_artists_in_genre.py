'''
Return songs from artists that became most hated when grouped together.
hated means their dislikes average climbed most significantly in their
common videos.
It returns songs in specified genre.
'''
MOST_HATED_PAIR_FROM_GENRE = {
    'query': '''
                SELECT DISTINCT youtube_video_id, youtube_video_title, video_id
                FROM artist_song_video_view, (
                    SELECT pairs.artist_id, ABS(pair_score - AVG(dislikes)) AS hated 
                    FROM (
                        SELECT song_id, artist_id, video_id, AVG(dislikes) AS pair_score
                        FROM artist_song_video_view
                        GROUP BY song_id, video_id
                        HAVING COUNT(artist_id) > 1) AS pairs, artist_song_video_view
                    WHERE pairs.artist_id = artist_song_video_view.artist_id
                    GROUP BY artist_id
                    ORDER BY hated DESC
                ) AS artist_hated 
                WHERE artist_hated.artist_id = artist_song_video_view.artist_id
                AND genre='%s'
                ORDER BY hated
                LIMIT 10
             ''',
    'mode'  : 'select',
    'args' : ['genre']
}