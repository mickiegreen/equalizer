MOST_LIKED_SONGS = {
    'query': '''SELECT `year`, youtube_video_id, youtube_video_title 
               FROM 
               (SELECT youtube_video_id, youtube_video_title, `year` 
               FROM( 
               SELECT youtube_video_title as title,youtube_video_id as id , YEAR(release_date) AS `year`, 
                sum(0.3*views+0.5*likes+0.2*comments) AS rating 
               FROM join_song_video_artist 
               WHERE country IN(select country from song where YEAR(release_date) = "%s") 
               GROUP BY id) rating_table 
               JOIN youtube_video  as main_table ON rating_table.id = main_table.youtube_video_id 
               ORDER BY rating  desc 
               limit 10) as a ''',
    'args': ['year'],
    'mode'  : 'select',
}

SELECT_YEAR = {
    'query' : '''
                SELECT DISTINCT(YEAR(release_date)) as `year` FROM song
              ''',
    'mode'  : 'select'
}