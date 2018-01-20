'''
This is a query to handle the sign up process.
We insert a new row to 'user' table with 3 attributes - user_name, email and password.
'''
SIGN_USER = {
    'query' : 'INSERT INTO user (user_name, email, password) VALUES ("%s", "%s", "%s")',
    'mode'  : 'insert',
    'args'  : ['user_name', 'email', 'password'],
    'default'   : {
        'user_name' : ''
    }
}