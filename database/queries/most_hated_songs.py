"""

"""
MOST_HATED_SONGS = {
    'query': '''
               SELECT `year`, youtube_video_id, youtube_video_title 
               FROM 
               (SELECT `year`,`id`, title 
               FROM( 
               SELECT YEAR(release_date) AS `year`,youtube_video_title AS title,youtube_video_id AS `id` , 
               SUM(0.3*views+0.5*likes+0.2*comments) AS rating 
               FROM join_song_video_artist 
               WHERE country IN(SELECT country FROM song WHERE YEAR(release_date) = "%s") 
               GROUP BY id) rating_table 
               JOIN youtube_video  AS main_table ON rating_table.id = main_table.youtube_video_id 
               ORDER BY rating  
               limit 10 ) AS a ''',
    'args': ['year'],
    'mode'  : 'select',
}