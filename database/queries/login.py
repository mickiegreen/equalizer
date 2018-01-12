USER_LOGIN = {
    'query' : 'SELECT (COUNT(*) > 0) AS login, user_id, user_name '
              'FROM ('
              'SELECT user_id, user_name '
              'FROM user '
              'WHERE email="%s" AND password="%s"'
              ') AS x',
    'mode'      : 'select',
    'args'      : ['email', 'password'],
}