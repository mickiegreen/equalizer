'''
Return songs from genres most common in specified country.
common means had the highest number of songs.
'''
MOST_COMMON_GENRE_IN_COUNTRY = {
    'query': '''
                SELECT DISTINCT video_id, youtube_video_id, youtube_video_title 
                FROM artist_song_video_view
                WHERE genre IN (
                    SELECT genres.genre
                    FROM song, (
                        SELECT DISTINCT genre, COUNT(song_id) AS common
                        FROM song
                        WHERE country="%s"
                        GROUP BY genre
                        HAVING common >= ALL (
                            SELECT COUNT(song_id) AS common
                            FROM song
                            WHERE country="%s"
                            GROUP BY genre
                        )
                    ) AS genres
                    WHERE genres.genre=song.genre 
                ) LIMIT 10
             ''',
    'mode'  : 'select',
    'args' : ['country', 'country']
}