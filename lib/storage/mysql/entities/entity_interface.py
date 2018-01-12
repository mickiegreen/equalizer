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

class EntityInterface(object):
    """ MySQL Entity interface """

    def dict(self):
        """ to dict without dumping value """
        raise NotImplementedError

    def keys(self):
        """ keys entry should have """
        raise NotImplementedError

    def values(self):
        """ current values of entry """
        raise NotImplementedError

    def table(self):
        """ entry table name """
        raise NotImplementedError

    def json(self):
        """ convert object to json """
        raise NotImplementedError

    def update(self, **kwargs):
        """ update object attributes """
        raise NotImplementedError

    def copy(self):
        """ create copy of object """
        raise NotImplementedError

    def primary_key(self):
        """ return object primary key """
        raise NotImplementedError

    def set_primary_key(self, key):
        """ set primary key """
        raise NotImplementedError

    def insert_query(self):
        """ insert query to execute """
        raise NotImplementedError

    def select_query(self):
        """ build select query """
        raise NotImplementedError

    def update_query(self):
        """ build update query """
        raise NotImplementedError

    def remove_query(self):
        """ build remove query"""
        raise NotImplementedError

    def remove_all_references_query(self):
        """
        build query that removes entry and all associated entries
        (i.e. foreign keys references)
        """
        raise NotImplementedError

    def select_all_query(self):
        """ build select * from table query """
        raise NotImplementedError

    def is_view(self):
        """ return True if not real table """
        raise NotImplementedError

    def primary_key_name(self):
        """ return primary key column name """
        raise NotImplementedError

    def split_to_real_entities(self):
        """
        in case entity isn't standalone (view. etc)
        return original entities
        """
        raise NotImplementedError
