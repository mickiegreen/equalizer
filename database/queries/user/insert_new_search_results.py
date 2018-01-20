INSERT_NEW_SEARCH_RESULTS = {
    'query' :   """
                INSERT INTO results_history (user_id, video_id)
                SELECT user_id, video_id
                FROM user, youtube_video AS v
                WHERE user_id=%d AND video_id IN (%s)
                ON DUPLICATE KEY UPDATE last_update=CURRENT_TIMESTAMP()
                """
                ,
    'args'  : ['user_id', 'data'],
    'mode'  : 'insert'
}