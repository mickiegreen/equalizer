'''
A query to show a specific user history search.
Going through his history and bringing back the last 5 searched videos.
'''
SHOW_HISTORY_PAGE = {
    'query': '''
            SELECT youtube_video_id 
            FROM youtube_video, (
            SELECT video_id,search_date 
            FROM history_results JOIN user_search_history
            ON history_results.history_id = user_search_history.history_id
            WHERE user_search_history.user_id ="%d") as user_history
            WHERE youtube_video.video_id=user_history.video_id
            ORDER BY search_date desc 
            LIMIT 5''',
    'args': ['user_id'],
    'mode'  : 'select'
}

