from .entity import Entity
import equalizer.config as app

class UserSearchHistory(Entity):
    _table = app.USER_SEARCH_HISTORY_TABLE
    _pk = app.USER_SEARCH_HISTORY_TABLE_PK
    _existsQuery = app.USER_SEARCH_HISTORY_EXISTS_QUERY

    def __init__(self, history_id = 0, user_id = None, params = None, search_date = None, **kwargs):
        self.history_id = history_id
        self.user_id = user_id
        self.params = params
        self.search_date = search_date