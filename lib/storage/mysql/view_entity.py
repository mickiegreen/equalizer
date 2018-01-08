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

from .abstract_entity import AbstractEntity
from overrides import overrides

class ViewEntity(AbstractEntity):
    """ MySQL view entity adapter """

    def __init__(self, view, primary_key, select_query, tables_entities,
                 remove_all_references = None, **kwargs):
        if not hasattr(primary_key, '__iter__'):
            raise ValueError("view entity primary key must be iterable")

        super(ViewEntity, self).__init__(
            view, primary_key,
            select_query, remove_all_references
        )

        self._primary_key = primary_key
        self._tables_entities = tables_entities

    @overrides
    def primary_key(self):
        """ return object primary key """
        return (getattr(self, k) for k in self._primary_key)

    @overrides
    def set_primary_key(self, key):
        """ set entry primary key """
        if not hasattr(key, '__iter__'):
            raise ValueError("view entity primary key must be iterable")

        # set full key
        for k, v in dict(zip(self.primary_key_name(), self.primary_key())):
            setattr(self, self._primary_key, key)

    @overrides
    def insert_query(self):
        """ execute insert query, must have engine set """
        raise NotImplementedError

    @overrides
    def remove_query(self):
        """ execute insert query, must have engine set """
        if not hasattr(self, 'engine'):
            raise ArithmeticError("view must have engine set before executing insert_query")

        engine = self.engine

        # splitting to real entities
        entities = self.split_to_real_entities()

        # safely remove each
        for entity in entities:
            engine.remove_safe(entity)

    @overrides
    def is_view(self):
        """ return True """
        return True

    @overrides
    def split_to_real_entities(self):
        """ return original entities """

        entities_map = {
            subclass().table() : subclass for subclass in AbstractEntity.__subclasses__() if subclass != ViewEntity
        }

        real_entities = []

        for entity_name in self._tables_entities:
            entity_cls = entities_map.get(entity_name, None)

            if entity_cls == None:
                raise ValueError("no such table or view : " + entity_name)

            real_entity = entity_cls(**self.dict())
            real_entities.append(real_entity)

        return real_entities

    def updatable(self):
        """ return True if updatable """
        raise NotImplementedError



