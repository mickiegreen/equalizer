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

from equalizer.lib.storage.mysql import MySqlEngine

class MysqlApi(object):
    """ MySQL Api to execute query """

    def __init__(self, engine):
        """
        :param engine: mysql storage engine
        """

        if not isinstance(engine, MySqlEngine):
            raise TypeError("Type of engine must be MySqlEngine")

        self.engine = engine

    def execute(self, query, mode, default = {}, args = [], params = {}):
        """
        executing query according to its type
        :param query: query object to execute
        """

        q_params = default.copy()
        q_params.update(params)
        params = q_params

        if mode not in ['select', 'update', 'insert', 'delete']:
            raise ValueError("Mode must be string with values "
                             "'select', 'update', 'insert', 'delete'.")

        for arg in args:
            if arg not in params.keys():
                return {
                    'rc' : -1,
                    'errorMsg'  : 'Request is missing parameters. Must have %s' %(','.join(args)),
                    'content'   : None
                }

        # building query
        try:
            query = self.build_query(query, args, params)

        except KeyError as e:
            return {
                'rc' : -1,
                'errorMsg'  : 'Request is missing parameters. Must have %s' %(','.join(args)),
                'content'   : None,
                'errorApi'  : e.message
            }
        except Exception as e:
            print e
            print 'following query unsuccessful\n'
            print query

        print query

        # executing according to mode
        if mode == 'insert': return self.insert(query)

        elif mode == 'select': return self.select(query)

        elif mode == 'update': return self.update(query)

        elif mode == 'delete': return self.delete(query)

    def insert(self, query):
        """
        insert object to database and return new object id
        """

        content = { 'id' : -1 }

        try:
            with self.engine.connection() as conn:
                cursor = conn.cursor()

                cursor.execute(query)
                conn.commit()

                content['id'] = int(cursor.lastrowid)

                return { 'rc' : 0, 'errorMsg' : '', 'content' : content }

        except Exception as e:
            return {'rc' : -1, 'errorMsg' : e.message, 'content' : content }

    def select(self, query):
        """
        return list of jsons from select
        """

        content = { 'data': [] }

        try:
            with self.engine.connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query)

                data = []

                # getting data
                for row in cursor.fetchall():
                    # creating json
                    data.append(dict(zip([_desc[0] for _desc in cursor.description], row)))

            content['data'] = data
            return { 'rc' : 0, 'errorMsg' : '', 'content' : content }

        except Exception as e:
            return {'rc': -1, 'errorMsg': e.message, 'content': content}

    def update(self, query):
        """
        update object and return its id if succeeded
        """
        content = {'data': []}

        try:
            with self.engine.connection() as conn:
                cursor = conn.cursor()

                cursor.execute(query)
                conn.commit()

                return {'rc': 0, 'errorMsg': '', 'content': content}

        except Exception as e:
            return {'rc': -1, 'errorMsg': e.message, 'content': content}

    def delete(self, query):
        """
        return list of jsons from select
        """
        try:
            with self.engine.connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()

                return {'rc': 0, 'errorMsg': ''}

        except Exception as e:

            return {'rc': -1, 'errorMsg': e.message}

    def build_query(self, query, params = [], values = {}):
        """ inject values to query in right order """
        return query %tuple([values[param] for param in params])

