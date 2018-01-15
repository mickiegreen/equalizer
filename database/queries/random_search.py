'''
This is a query to add a search to the user pool of queries.
The query updates 'user_search_history' table.
It updates the 'is_favorite' attribute of a specific search to 1.
'''
RANDOM_SEARCH = {
    'query' : 'UPDATE user_search_history '
              'SET is_favorite=1 '
              'WHERE history_id=%d',
    'args': ['history_id'],
    'mode'  : 'select',
    'default':{
        'user_name' : ''
    }
}