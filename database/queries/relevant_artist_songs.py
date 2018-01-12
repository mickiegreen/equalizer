RELEVANT_ARTIST_SONGS = {
    'query' :
                'SELECT youtube_video_id, youtube_video_title'
                
                'from    join_song_video_artist'
                
                'where  artist_id           in'
                
                '(select artist_id'
                
                'from     join_song_artist'
                
                'where  YEAR(CURDATE())-YEAR(release_date) <= 5'
                
                'group by  artist_id)'
                
                'group by youtube_video_id'
                'limit 10',


    'mode'  : ['select']

}