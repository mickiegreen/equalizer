'''
Get most hated artist in given years range.
Hated means got most dislikes during these
years on one of his videos.
'''
MOST_HATED_ARTISTS_SINCE_YEAR = {
    'query': '''
            SELECT youtube_video_id, youtube_video_title, video_id, FORMAT(FLOOR(SUM(dislikes)),0) AS hated_score
            FROM artist_song_video_view asv, (
                SELECT DISTINCT artist_id
                FROM artist_song_view
                WHERE EXISTS (
                    SELECT artist_id
                    FROM artist_song_view
                    WHERE YEAR(release_date) > %d
                ) 
            ) AS artist_in_years, artist_statistics
            WHERE artist_in_years.artist_id=asv.artist_id AND artist_statistics.artist_id=asv.artist_id
            GROUP BY video_id
            ORDER BY hated, popularity DESC
            LIMIT 10
             ''',
    'mode'  : 'select',
    'args' : ['year']
}