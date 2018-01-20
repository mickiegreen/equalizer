'''
A query to show a specific user history search.
Going through his history and bringing back the last 10 searched videos.
'''
GET_USER_RECENT_HISTORY = {
    'query':    'SELECT v.video_id AS video_id, youtube_video_id, youtube_video_title '
                'FROM youtube_video v, results_history r '
                'WHERE v.video_id=r.video_id '
                'AND r.user_id=%d '
                'ORDER BY r.last_update DESC '
                'LIMIT 10',
    'args': ['user_id'],
    'mode'  : 'select'
}

