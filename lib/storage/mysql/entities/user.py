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

from ..abstract_entity import AbstractEntity as Entity
from ..attributes import PrimaryKey, VarcharAttribute

import config as app

class User(Entity):
    """ user table entity """

    def __init__(self, user_id = 0, name = None, email = None, passwd = None, **kwargs):
        super(User, self).__init__(
            table=app.USER_TABLE,
            primary_key=app.USER_TABLE_PK,
            select_query=app.USER_EXISTS_QUERY
        )

        self.user_id = PrimaryKey('user_id', user_id)
        self.name = VarcharAttribute('name', name)
        self.email = VarcharAttribute('email', email)
        self.passwd = VarcharAttribute('passwd', passwd)