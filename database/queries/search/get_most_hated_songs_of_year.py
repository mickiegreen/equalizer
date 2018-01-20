"""
return most hated songs in specified year
"""
MOST_HATED_SONGS_OF_YEAR = {
    'query': '''
                SELECT youtube_video_id AS youtube_video_id, youtube_video_title, video_id 
                FROM (
                  SELECT `year`, main_table.youtube_video_id, youtube_video_title, video_id
                  FROM ( 
                    SELECT YEAR(release_date) AS `year`, youtube_video_id,
                      SUM(0.3*views+0.5*likes+0.2*comments) AS rating 
                    FROM artist_song_video_view 
                    WHERE country IN(SELECT country FROM song WHERE YEAR(release_date) = %d) 
                    GROUP BY youtube_video_id) 
                  AS rating_table 
                  JOIN youtube_video AS main_table ON rating_table.youtube_video_id = main_table.youtube_video_id
                  ORDER BY rating  
                  LIMIT 10 
                ) AS a
            ''',
    'args': ['year'],
    'mode'  : 'select',
}