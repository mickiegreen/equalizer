HATED_GENRE_SONGS = {
    'query':'''
            SELECT  youtube_video_id, youtube_video_title 
            FROM    (SELECT youtube_video_id, youtube_video_title,sum(0.3*views+0.5*likes+0.2*comments) AS rating 
            FROM    join_song_video_artist 
            WHERE   genre=( 
            SELECT  genre 
            FROM    ( 
            SELECT  genre , sum(views) 
            FROM    join_song_video_artist
            GROUP BY genre 
            ORDER BY  sum(views)  
            LIMIT 1) as genre_table) 
            GROUP BY  video_id 
            ORDER BY  rating  
            LIMIT  10) as  worst_song ''',
    'mode': 'select'

}