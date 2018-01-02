from .entity import Entity
import equalizer.config as app

class User(Entity):
    _table = app.USER_TABLE
    _pk = app.USER_TABLE_PK
    _existsQuery = app.USER_EXISTS_QUERY

    def __init__(self, user_id = 0, name = None, email = None, passwd = None, **kwargs):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.passwd = passwd