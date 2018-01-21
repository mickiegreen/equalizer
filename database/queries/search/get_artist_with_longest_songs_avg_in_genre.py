'''
Following query returns songs of artist with longest duration average, who has
at list one song in specified genre.
First it fetches the duration average of each artist (nested query), then filter
videos by the artist ids that remained
'''
ARTIST_WITH_LONGEST_SONGS_AVG_IN_GENRE = {
    'query': '''
            SELECT youtube_video_id, youtube_video_title, video_id
            FROM (
                SELECT artist_id, AVG(duration) AS duration_avg
                FROM artist_song_view
                WHERE song_id = ANY(
                    SELECT song_id
                    FROM song
                    WHERE genre='%s'
                )
                GROUP BY artist_id
                HAVING duration_avg >= ALL (
                    SELECT AVG(duration) AS duration_avg
                    FROM artist_song_view
                    WHERE song_id = ANY(
                        SELECT song_id
                        FROM song
                        WHERE genre='%s'
                    )
                    GROUP BY artist_id
                )
            ) AS artist_duration, artist_song_video_view
            WHERE artist_duration.artist_id=artist_song_video_view.artist_id
            LIMIT 10
            ''',
        'mode': 'select',
        'args': ['genre', 'genre']
}