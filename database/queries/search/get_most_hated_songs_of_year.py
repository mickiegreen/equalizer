"""
return most hated songs in specified year
"""
MOST_HATED_SONGS_OF_YEAR = {
    'query': '''
              SELECT `year`, main_table.youtube_video_id, youtube_video_title, video_id
              FROM ( 
                SELECT YEAR(release_date) AS `year`, youtube_video_id,
                  0.3*SUM(views)+0.5*SUM(dislikes)+0.2*SUM(comments) AS rating 
                FROM artist_song_video_view 
                WHERE country IN(
                  SELECT DISTINCT country FROM song
                  WHERE YEAR(release_date) = %d
                ) 
                GROUP BY youtube_video_id) 
              AS rating_table 
              JOIN youtube_video AS main_table ON rating_table.youtube_video_id = main_table.youtube_video_id
              ORDER BY rating  
              LIMIT 10;
            ''',
    'args': ['year'],
    'mode'  : 'select',
}