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

from data_interface import DataHandler
from equalizer.lib.storage.mysql import MySqlEngine

class AbstractDataHandler(DataHandler):
    """
    abstract data adapter to handler
    new and existing data in storage
    """

    def __init__(self, engine):
        """ storage engine to handle data """
        if not isinstance(engine, MySqlEngine):
            raise TypeError("engine must be of type MySqlEngine")

        self.engine = engine

    def add(self, data):
        """ adding data to of type to storage """
        raise NotImplementedError

    def add_if_valid(self, data):
        """
        validating data and if not valid not added without error
        """
        if not self.validate(data):
            return -1

        return self.add(data)

    def add_all(self, data):
        """
        :param data: add many entries to storage
        """

        if not hasattr(data, '__iter__'):
            raise TypeError(" data must be iterable ")

        for entry in data:
            # add to db if ok, else skip
            self.add_if_valid(entry)

    def add_from_local_folder(self, folder, limit = 20000, update = True):
        """
        add entries from file system
        :param folder - directory to fetch files from:
        :param limit - max num of records to add
        """
        raise NotImplementedError

    def update(self, data):
        """ update existing data """
        raise NotImplementedError

    def update_all(self):
        """ update all entries in db """
        raise NotImplementedError

    def get(self, data):
        """ get existing data from storage """
        raise NotImplementedError

    def get_all(self):
        """ return all data from storage """
        raise NotImplementedError

    def exists(self, data):
        """ return True if data exists in storage else False """
        raise NotImplementedError

    def remove(self, data):
        """ remove data from storage """
        raise NotImplementedError

    def remove_all(self):
        """ clear all data """
        raise NotImplementedError

    def uptodate(self, data):
        """ return True if data is up-to-date else False """
        raise NotImplementedError

    def get_more_data(self, params = {}, limit = 2000):
        """
        add new entries to database
        @limit - max num of records to add
        @params - search query
        """
        raise NotImplementedError

    def validate(self, data):
        """
        :param data: validate
        :return: True if data llegal
        """
        raise NotImplementedError
