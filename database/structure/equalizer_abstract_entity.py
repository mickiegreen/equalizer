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

from equalizer.lib.storage.mysql.entities import AbstractEntity
import structure_config as app

class EqualizerAbstractEntity(AbstractEntity):
    """ MySQL Generic equalizer entity adapter """

    def __init__(self, table, primary_key, select_query,
                 remove_all_references = None):
        super(EqualizerAbstractEntity, self).__init__(
            table = table,
            primary_key = primary_key,
            select_query = select_query,
            remove_all_references=remove_all_references,
            update_query = app.UPDATE_QUERY,
            select_all_query=app.SELECT_ALL_QUERY,
            remove_query=app.REMOVE_QUERY,
            insert_query=app.INSERT_QUERY,
        )
