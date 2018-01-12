
LONGEST_ARTIST_SONG = {
    'query' :
            'SELECT youtube_video_id,youtube_video_title ' 
            'FROM join_song_video_artist ' 
            'where artist_id IN ( '
            'SELECT A.artist_id '
            'From '
            '(select artist_id, avg(duration) as artist_avg, count(*) as artist_cnt '
            'From join_song_artist '
            'Group by artist_id '
            ') AS A , join_song_artist '
            'Where join_song_artist.artist_id = A.artist_id '
            'and A.artist_avg<= join_song_artist.duration '
            'Group by  A.artist_id '
            'Having count(*) >= 50 '
            ') '
            'group by artist_id '
            'limit 10 ',
    'mode'  : 'select'
}


