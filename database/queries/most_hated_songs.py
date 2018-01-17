import random

MOST_HATED_SONGS = {
    'query': '''
               SELECT `year`, youtube_video_id, youtube_video_title 
               FROM 
                   (SELECT `year`,youtube_video_id, youtube_video_title 
                   FROM( 
                       SELECT YEAR(release_date) as `year`,youtube_video_title as title,youtube_video_id as id , 
                        sum(0.3*views+0.5*likes+0.2*comments) AS rating 
                       FROM join_song_video_artist 
                       WHERE country IN(select country from song where YEAR(release_date) = "%s") 
                       GROUP BY id) rating_table 
                   JOIN youtube_video  as main_table ON rating_table.id = main_table.youtube_video_id 
                   ORDER BY rating  
                   limit 10 ) as a ''',

    'args': ['year'],
    'mode'  : 'select',
    'default' : {"year":random.randint(1905,2018)}
}