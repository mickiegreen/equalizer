# -*- coding: utf-8 -*-

# Copyright (c) 2018 Michael Green
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from equalizer.lib.storage.mysql.attributes import PrimaryKey, DatetimeAttribute, \
    VarcharAttribute, IntegerAttribute

from equalizer_abstract_entity import EqualizerAbstractEntity as Entity
import structure_config as app

class UserSearchHistory(Entity):
    """ user search history table entity """

    def __init__(self, history_id = 0, user_id = None, params = None, search_date = None, **kwargs):
        super(UserSearchHistory, self).__init__(
            table=app.USER_SEARCH_HISTORY_TABLE,
            primary_key=app.USER_SEARCH_HISTORY_TABLE_PK,
            select_query=app.USER_SEARCH_HISTORY_EXISTS_QUERY
        )
        self.history_id = PrimaryKey('history_id', history_id)
        self.user_id = IntegerAttribute('user', user_id)
        self.params = VarcharAttribute('params', params)
        self.search_date = DatetimeAttribute('search_date', search_date)