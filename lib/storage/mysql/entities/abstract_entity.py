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
from overrides import overrides

from .entity_interface import EntityInterface

class AbstractEntity(EntityInterface):
    """ MySQL Generic entity adapter """

    def __init__(self, table, primary_key, select_query,
                 insert_query, remove_query, update_query,
                 select_all_query, remove_all_references = None):

        self._table = table
        self._primary_key = primary_key
        self._select_query = select_query
        self._insert_query = insert_query
        self._update_query = update_query
        self._remove_query = remove_query
        self._select_all_query = select_all_query
        self._remove_all_references = remove_all_references

        self._white_list = ['_table', '_primary_key',
                            '_select_query',
                            '_update_query',
                            '_insert_query',
                            '_remove_query',
                            '_remove_all_references',
                            '_tables_entities',
                            '_select_all_query',
                            '_white_list', 'engine', '_engine']

    @overrides
    def dict(self):
        """ to dict without dumping value """
        return {k : v for k, v in self}

    @overrides
    def keys(self):
        """ keys entry should have """
        return self.json().keys()

    @overrides
    def values(self):
        """ current values of entry """
        return self.json().values()

    @overrides
    def table(self):
        """ return entry table """
        return self._table

    @overrides
    def json(self):
        """ convert object to json """
        return {k : repr(getattr(self, k)) for k, v in self}

    @overrides
    def update(self, **kwargs):
        """ update object attributes """
        for k, v in kwargs.iteritems():
             self[k] = v

    @overrides
    def copy(self):
        """ create copy of object """
        return self.__class__(**self.dict())

    @overrides
    def primary_key(self):
        """ return object primary key """
        return self[self._primary_key]

    @overrides
    def set_primary_key(self, key):
        """ set entry primary key """
        self[self._primary_key] = key

    @overrides
    def insert_query(self):
        """ build insert query """
        cols = [k for k in self.keys()]
        vals = [v for v in self.values()]

        return self._insert_query %(self.table(), ','.join(cols), ','.join(vals))

    @overrides
    def select_query(self):
        """ build select query """
        keys = self._select_query.get('keys', [])

        # getting values int proper format
        keys = tuple(repr(getattr(self, key)) for key in keys)

        # building string using values
        return self._select_query.get('query', '') % keys

    @overrides
    def update_query(self):
        """ build update query """

        # building vals list to set
        vals = ','.join([ k + '=' + repr(getattr(self, k)) for k, v in self ])

        # final query
        return self._update_query %(self.table(), vals, self._primary_key, self.primary_key())

    @overrides
    def remove_query(self):
        """ build remove query"""
        return self._remove_query %(self.table(), repr(getattr(self, self._primary_key)), self.primary_key())

    @overrides
    def remove_all_references_query(self):
        """
        build query that removes entry and all associated entries
        (i.e. foreign keys references)
        :default - regular remove
        """
        if self._remove_all_references == None:
            return self.remove_query()

        else:
            keys = self._remove_all_references.get('keys', [])
            keys = tuple(repr(self[key]) for key in keys)
            return self._remove_all_references.get('query', '') % keys

    @overrides
    def select_all_query(self):
        """ build select * from table query """
        return self._select_all_query %(self.table())

    @overrides
    def is_view(self):
        """ return True if not real table """
        return False

    @overrides
    def primary_key_name(self):
        """ return primary key column name """
        return self._primary_key

    @overrides
    def split_to_real_entities(self):
        """
        in case entity isn't standalone (view. etc)
        return original entities
        """
        return [self]

    def __getitem__(self, item):
        """ define [] get operator for entity """

        # if item exists and isn't hidden - return it
        if hasattr(self, item) and item not in self._white_list:
            return getattr(self, item).value()

        else:
            return None

    def __setitem__(self, key, value):
        """ define [] set operator for entity """
        if hasattr(self, key):
            getattr(self, key).set(value)

    def __iter__(self):
        """ iter entity as json """
        for k, v in self.__dict__.iteritems():
            if k not in self._white_list:
                yield (v.key(), v.value())

    def __eq__(self, other):
        """ compare two entries """

        # if not entry class return False
        if not isinstance(self.__class__, other):
            return False

        # compare each key
        for k, v in other:
            if not self[k].equals(v) : return False

        return True

    def __repr__(self):
        """ print object as json """
        return json.dumps(self.json(), indent=4, sort_keys=True)

