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

class StorageEngine(object):
    """ Storage adapter interface for storing data """

    def get(self, entry):
        """ fetch from storage """
        raise NotImplementedError

    def get_all(self, entries):
        """ fetch all from storage """
        raise NotImplementedError

    def add(self, entry):
        """add new entry to database"""
        raise NotImplementedError

    def add_all(self, entries):
        """ add new entries (list) to relation """
        raise NotImplementedError

    def add_if_not_exists(self, entry):
        """ if entry exists in database return its id else add it """
        raise NotImplementedError

    def remove(self, entry):
        """ remove entry from relation """
        raise NotImplementedError

    def remove_all(self, entries):
        """ remove list of entries """
        raise NotImplementedError

    def update(self, entry):
        """ update entry data """
        raise NotImplementedError

    def update_all(self, entries):
        """ update all entries (list) """
        raise NotImplementedError

    def update_if_exists_else_add(self, entry):
        """ update entry if exists, if not add it to storage """
        raise NotImplementedError

    def truncate(self):
        """ remove all entries from storage """
        raise NotImplementedError

    def live_update(self, relation, override = True):
        """ add more entries to relation """
        raise NotImplementedError