'''
This is a query to handle the login process.
It requires three arguments - login, user_id and user_name.
login is 1 if the inserted details are correct, 0 otherwise.
user_id and user_name are attributes in "user" table.
'''
LOGIN_AUTH = {
    'query' : 'SELECT (COUNT(*) > 0) AS login, user_id, user_name '
              'FROM ('
              'SELECT user_id, user_name '
              'FROM user '
              'WHERE email="%s" AND password="%s"'
              ') AS x',
    'mode'      : 'select',
    'args'      : ['email', 'password'],
}