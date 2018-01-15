'''
This is a query which selects top 10 most 'digging' music videos.

'''
LONGEST_ARTIST_SONG = {
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
                                        )
        GROUP BY song_id
        ORDER BY TOT.duration, ARTI.artist_avg DESC
        LIMIT 10''',
        'mode': 'select'
}


