REMOVE_USER_OLD_HISTORY = {
    'query' :   'DELETE FROM results_history '
                'WHERE user_id=%d AND result_id NOT IN (%s) ',
    'args'  :   ['user_id', 'result_ids'],
    'mode'  :   'delete'
}