'''
This is a query which selects top 10 most 'digging' music videos.

'''
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
HARELZ_LONGEST_ARTIST_SONG = {
        'query':'''
        SELECT youtube_video_title, youtube_video_id
        FROM join_song_video_artist as TOT, 
            (SELECT IN_ART.artist_id, avg(IN_ART.duration) as artist_avg
            FROM join_song_video_artist AS IN_ART
            GROUP BY IN_ART.artist_id
            HAVING count(*)>= 3
            ) AS ARTI
        WHERE TOT.artist_id = ARTI.artist_id
        AND TOT.artist_id IN (	SELECT distinct Z.artist_id
                                FROM join_song_video_artist AS Z
                                WHERE (SELECT avg(S.duration)
                                FROM song AS S) <=  ALL(SELECT duration
                                                        FROM join_song_video_artist AS X
                                                        WHERE X.artist_id = Z.artist_id)
                                AND artist_id != 248
                            )
        GROUP BY song_id
        ORDER BY TOT.duration, ARTI.artist_avg DESC
        LIMIT 10''',
        'mode': 'select'
}


