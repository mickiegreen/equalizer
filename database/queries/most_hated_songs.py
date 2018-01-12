MOST_HATED_SONGS = {
    'query' : 'UPDATE user_search_history '
              'SET is_favorite=1 '
              'WHERE history_id=%d',
    'params': ['history_id'],
    'mode'  : ['select'],
    'default':{
        'user_name' : ''
    }
}