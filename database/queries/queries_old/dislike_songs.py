'''
This is a query which selects top 10 disliked music videos.
This query returns music videos by an artist who has total of dislikes
in all of his music videos combined bigger then the minimum sum of dislikes by an artist
who has total of more than 1000 likes, yet less then the maximum sum of dislikes by an artist
who has total of more then 10000 likes.
Then return 10 music videos one by each artist.
'''
DISLIKED_SONGS = {
    'query': '''
            SELECT      youtube_video_id, youtube_video_title 
            FROM( 
            SELECT      sum(dislikes) as dislike,youtube_video_id, youtube_video_title 
            FROM        artist_song_video_view 
            GROUP BY    (artist_id) 
            HAVING      dislike > 
            (SELECT     sum(dislikes) FROM artist_song_video_view GROUP BY (artist_id) HAVING sum(likes)>1000 ORDER BY sum(dislikes) ASC LIMIT 1) 
            AND         dislike < 
            (SELECT     sum(dislikes) FROM artist_song_video_view GROUP BY (artist_id) HAVING sum(likes)>10000 ORDER BY sum(dislikes) DESC LIMIT 1) 
            LIMIT       10 
            ) AS a ''',

    'mode'  : 'select'
}
