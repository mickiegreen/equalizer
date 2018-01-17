'''
A query to update a user history and mark the specific search to be a favorite search (save it).
'''
USER_HISTORY_SAVE = {
    'query' : 'UPDATE user_search_history '
              'SET is_favorite=1 '
              'WHERE history_id=%d',
    'params': ['history_id'],
    'mode'  : ['update']
}