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

import json

from .entity_interface import EntityInterface

import config as app

class AbstractEntity(EntityInterface):
    """ MySQL Generic entity adapter """

    def __init__(self, table, primary_key, select_query):
        self._table = table
        self._primary_key = primary_key
        self._select_query = select_query

    def table(self):
        """ return entry table """
        return self._table

    def json(self):
        """ convert object to json """
        _json = self.__dict__.copy()
        _json.pop('_table')
        _json.pop('_primary_key')
        _json.pop('_select_query')

        return _json

    def update(self, **kwargs):
        """ update object attributes """
        self.__init__(**kwargs)

    def copy(self):
        """ create copy of object """
        return self.json().copy()

    def primary_key(self):
        """ return object primary key """
        return getattr(self, self._primary_key)

    def set_primary_key(self, key):
        """ set entry primary key """
        setattr(self, self._primary_key, key)

    def insert_query(self):
        """ build insert query """

        cols = [k for k in self.json().keys()]
        vals = [str(self.json()[k]) for k in cols if self.json()[k] != None]

        return app.INSERT_QUERY %(self.table(), ','.join(cols), ','.join(vals))

    def select_query(self):
        """ build select query """
        keys = self._select_query.get('keys', [])
        keys = tuple(str(getattr(self, key)) for key in keys)
        return self._select_query.get('query', '') % keys

    def update_query(self):
        """ build update query """

        # building vals list to set
        sql_parser = lambda x: '"' + str(x) + '"' if str(x).count('\'') > 0 else "'" + str(x) + "'"
        vals = ','.join([ str(k) + '=' + sql_parser(v) for k, v in self.json().items() ])

        # final query
        return app.UPDATE_QUERY %(self.table(), vals, self._primary_key, self.primary_key())

    def remove_query(self):
        """ build remove query"""

        return app.REMOVE_QUERY %(self.table(), self._primary_key, str(self.primary_key()))

    def __eq__(self, other):
        """ compare two entries """

        # if not entry class return False
        if not isinstance(self.__class__, other):
            return False

        # compare each key
        for k, v in other.json().items():
            if self.json().get(k, None) != v: return False

        return True

    def __repr__(self):
        """ print object as json """
        return json.dumps(self.json(), indent=4, sort_keys=True)

