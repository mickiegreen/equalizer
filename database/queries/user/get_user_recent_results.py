'''
A query to show a specific user history search.
Going through his history and bringing back the last 10 searched videos.
'''
GET_USER_RECENT_RESULTS = {
    'query':    'SELECT result_id '
                'FROM results_history r '
                'WHERE r.user_id=%d '
                'ORDER BY r.last_update DESC '
                'LIMIT 50',
    'args': ['user_id'],
    'mode'  : 'select'
}

