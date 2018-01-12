USER_SIGN_UP = {
    'query' : 'INSERT INTO user (user_name, email, password) VALUES ("%s", "%s", "%s")',
    'mode'  : 'insert',
    'args'  : ['user_name', 'email', 'password'],
    'default'   : {
        'user_name' : ''
    }
}