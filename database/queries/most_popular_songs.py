USER_HISTORY_SAVE = {
    'query' : 'UPDATE user_search_history '
              'SET is_favorite=1 '
              'WHERE history_id=%d',
    'params': ['history_id'],
    'mode'  : ['update'],
    'default':{
        'user_name' : ''
    }
}