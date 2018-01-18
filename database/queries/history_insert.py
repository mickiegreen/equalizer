USER_HISTORY_COUNT= {
     'query': '''
            SELECT count(*) as count
            FROM history_results
            WHERE  user_id= '%d'
            AND video_id IN (select video_id 
            FROM  youtube_video
            WHERE youtube_video.youtube_video_id="%s")
        ''',
        'mode': 'select',
        'args': ['user_id','youtube_video_id']
}

USER_HISTORY_INSERT = {
     'query': '''
            INSERT INTO user_search_history 
            VALUES(0,'%d',CURDATE())
        ''',
        'mode': 'insert',
        'args': ['user_id']
}

MIDDLE_HISTORY_INSERT = {
     'query': '''
            INSERT INTO history_result 
            VALUES(0, %d,(select video_id 
            FROM  youtube_video
            WHERE youtube_video.youtube_video_id="%s"))
        ''',
        'mode': 'insert',
        'args': ['history_id','youtube_video_id']
}