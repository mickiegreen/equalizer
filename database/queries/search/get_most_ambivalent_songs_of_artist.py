'''
Return specified artist most ambivalent songs.
ambivalent means min abs distance between likes and dislikes ratio
'''
MOST_AMBIVALENT_SONGS_OF_ARTIST = {
    'query': '''
                SELECT DISTINCT youtube_video_id, youtube_video_title, video_id
                FROM (
                    SELECT song_id, ABS(ratio - (1 - ratio)) AS amb
                    FROM (
                        SELECT song_id, SUM(likes)/(SUM(likes)+SUM(dislikes)) AS ratio
                        FROM artist_song_video_view sva
                        WHERE artist_id=%d
                        GROUP BY song_id
                    ) AS song_ratio
                    ORDER BY amb
                ) AS amb_song, artist_song_video_view sva
                WHERE amb_song.song_id=sva.song_id
                ORDER BY amb
                LIMIT 10
             ''',
    'mode'  : 'select',
    'args' : ['artist_id']
}