'''
Return songs from artists that became most hated when grouped together.
hated means their dislikes average climbed most significantly in their
common videos.
It returns songs in specified genre.
'''
MOST_HATED_PAIR_FROM_GENRE = {
    'query': '''
                SELECT DISTINCT youtube_video_id, youtube_video_title, pairs.video_id AS video_id, FORMAT(FLOOR(
                    CASE WHEN SUM(dislikes)-hated1 > SUM(dislikes)-hated2 
                    THEN SUM(dislikes)-hated1 ELSE SUM(dislikes)-hated2 END),0)
                    AS pair_score
                FROM (
                    SELECT ar1.artist_id AS a1, ar1.hated AS hated1, 
                        ar2.artist_id AS a2, ar2.hated AS hated2, 
                        as1.song_id, video_id
                    FROM artist_statistics ar1, artist_statistics ar2, 
                        artist_song as1, artist_song as2, artist_song_video asv 
                    WHERE as1.song_id = as2.song_id
                        AND as1.artist_id=ar1.artist_id
                        AND as2.artist_id=ar2.artist_id
                        AND asv.artist_song_id=as1.artist_song_id
                    GROUP BY a1, a2
                    HAVING a1 < a2
                ) AS pairs, artist_song_video_view asvv
                WHERE asvv.video_id = pairs.video_id
                    AND asvv.artist_id = pairs.a1
                    AND genre="%s"
                GROUP BY a1, a2
                ORDER BY pair_score DESC
                LIMIT 10
             ''',
    'mode'  : 'select',
    'args' : ['genre']
}