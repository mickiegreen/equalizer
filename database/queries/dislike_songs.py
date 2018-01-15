
DISLIKES_SONGS = {
    'query': '''
            SELECT      youtube_video_id, youtube_video_title 
            FROM( 
            SELECT      sum(dislikes) as dislike,youtube_video_id, youtube_video_title 
            FROM        join_song_video_artist 
            GROUP BY    (artist_id) 
            HAVING      dislike > 
            (SELECT     sum(dislikes) FROM join_song_video_artist GROUP BY (artist_id) HAVING sum(likes)>1000 ORDER BY sum(dislikes) ASC LIMIT 1) 
            AND         dislike < 
            (SELECT     sum(dislikes) FROM join_song_video_artist GROUP BY (artist_id) HAVING sum(likes)>10000 ORDER BY sum(dislikes) DESC LIMIT 1) 
            LIMIT       10 
            ) AS a ''',
    'mode'  : 'select'
}
