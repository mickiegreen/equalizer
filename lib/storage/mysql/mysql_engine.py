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

from overrides import overrides

from mysql_tunnel_connection import MysqlTunnelConnection
from ..storage_engine import StorageEngine
from entities import AbstractEntity as Entity
import logging
logger = logging.getLogger()

class MySqlEngine(StorageEngine):
    """ Adapter to connect to MySQL db """

    def __init__(self, host, user, password, schema, port = 3306,
                 use_tunnel = False, ssh_port = 22, ssh_host = None,
                 ssh_user = None, ssh_passwd = None, remote_mysql_port = None,
                 remote_bind_address = None, local_bind_address = None):

        """ MySQL authentication details """
        self.mysql_auth_info = dict(
            host = host,
            user = user,
            password = password,
            port = port,
            schema = schema,
            use_tunnel = use_tunnel
        )

        self.ssh_tunnel_info = dict(
            ssh_host = ssh_host,
            ssh_port = ssh_port,
            ssh_user = ssh_user,
            ssh_passwd = ssh_passwd,
            remote_bind_address = remote_bind_address,
            remote_mysql_port = remote_mysql_port,
            local_bind_address = local_bind_address,
            use_tunnel = use_tunnel
        )

    def get(self, entry):
        """
        fetch from storage,
        updating entry with data fetched
        and returning entry id
        """

        # force entity object
        if not isinstance(entry, Entity):
            raise TypeError("Entry must be of type Entity")

        # fetch entry from db
        with self._connect() as conn:
            cur = conn.cursor()
            query = entry.select_query()

            logger.debug('Getting object from db')
            logger.debug(entry)
            logger.debug(query)

            count = cur.execute(query)

            # if entry exists update given entry
            if count > 0:
                data = self._toJson(cur.description, cur.fetchone())
                entry.update(**data)
                key = entry.primary_key()

            else: key = -1

        return key

    def get_all(self, entries):
        """ fetch all from storage """

        # force entries as list
        if not isinstance(entries, list):
            raise TypeError("Entities must be of type list")

        # get each
        for entry in entries:
            self.get(entry)

        return entries

    def exists(self, entry):
        """ return true of object exists """
        entry_copy = entry.copy()
        return self.get(entry_copy) == -1

    def add(self, entry):
        """add new entry to database and return new key"""

        # force entity object
        if not isinstance(entry, Entity):
            raise TypeError("Entry must be of type Entity")

        logger.debug("Adding entry - " + repr(entry))

        # if view add all entities to db
        if entry.is_view():

            # let view do his thing
            setattr(entry, 'engine', self)
            key = entry.insert_query()
            delattr(entry, 'engine')

            # return view key
            return key

        # not view - just insert
        key = self._execute(entry.insert_query())

        # update entry
        if key != -1: entry.set_primary_key(key)

        return key

    def add_all(self, entries):
        """ add new entries (list) to relation """

        # force entries as list
        if not isinstance(entries, list):
            raise TypeError("Entities must be of type list")

        for entry in entries:
            # force entity object
            if not isinstance(entry, Entity): raise TypeError("Entry must be of type Entity")

            # add entry
            self.add(entry)

    def add_if_not_exists(self, entry):
        """
        if entry exists in database return its id else add it
        :return primary_key
        """

        # force entity object
        if not isinstance(entry, Entity):
            raise TypeError("Entry must be of type Entity")

        # make a copy to avoid change the origin object
        entry_copy = entry.copy()

        # get object and if exists return
        key = self.get(entry_copy)

        if key == -1: return self.add(entry)

    def remove(self, entry):
        """
        remove entry from relation
        :return removed entry
        """
        # force entity object
        if not isinstance(entry, Entity):
            raise TypeError("Entry must be of type Entity")

        # saving removed entry to object
        data = entry.copy()
        key = self.get(data)

        # no such key
        if key == -1:
            raise ValueError("entry does not exist")

        # delete entry
        with self._connect() as cur:
            conn = cur.connection
            query = entry.remove_query()

            logger.debug("deleting entry")
            logger.debug(query)

            cur.execute(query)
            conn.commit()

        # return removed entry
        return data

    @overrides
    def remove_safe(self, entry):
        """ remove all entry references """

        # force entity object
        if not isinstance(entry, Entity):
            raise TypeError("Entry must be of type Entity")

        # if entry is view - let it do its thing
        if entry.is_view():
            setattr(entry, 'engine', self)
            entry.remove_all_references_query()
            delattr(entry, 'engine')

        # if regular entity - execute query
        else:
            self._execute(entry.remove_all_references_query())

    def remove_all(self, entries):
        """
        remove list of entries
        :return removed entries
        """

        # force entries as list
        if not isinstance(entries, list):
            raise TypeError("Entities must be of type list")

        # removing entries
        removed = []
        for entry in entries: removed.append(self.remove(entry))

        return removed

    def update(self, entry):
        """ update entry data """

        # force entity object
        if not isinstance(entry, Entity):
            raise TypeError("Entry must be of type Entity")

        # update entry
        for real_entity in entry.split_to_real_entities():
            self._execute(real_entity.update_query())

        return entry.primary_key()

    def update_all(self, entries):
        """ update all entries (list) """

        # force entries as list
        if not isinstance(entries, list):
            raise TypeError("Entities must be of type list")

        for entry in entries: self.update(entry)

    def update_if_exists_else_add(self, entry):
        """ update entry if exists, if not add it to storage """

        # force entity object
        if not isinstance(entry, Entity):
            raise TypeError("Entry must be of type Entity")

        # make copy to avoid override
        entry_copy = entry.copy()
        key = self.get(entry_copy)

        # if not exist add it
        if key == -1: return self.add(entry)

        # else update entry and return key
        entry.set_primary_key(key)
        self.update(entry)
        return entry.primary_key()

    def truncate(self, entry):
        """ remove all entries from storage """

        # TODO fix query to truncate tables
        query = ''

        with self._connect() as cur:

            # getting connection object
            conn = cur.connection

            logger.debug("Execute query:")
            logger.info(query)
            logger.debug(conn.__dict__)

            try:

                # execute & commit query
                cur.execute(query)
                conn.commit()

            except Exception as e:
                # rollback if error
                conn.rollback()
                logger.error(e)

    def live_update(self, relation, override = True):
        """ add more entries to relation """

        #TODO implement
        pass

    def fetch_all_like_entry(self, entry):
        """ build select * from table query """

        if not isinstance(entry, Entity):
            raise TypeError("entry nust be of type entity")

        # fetching all entries from database
        with self._connect() as conn:
            cur = conn.cursor()

            # executing query
            query = entry.select_all_query()
            cur.execute(query)

            data = []

            # getting data
            for row in cur.fetchall():

                # creating new object for each entry in table
                new_data = entry.__class__(**self._toJson(cur.description, row))

                # adding to final data
                data.append(new_data)

        return data

    def connection(self):
        """ return new object connection """
        return self._connect()

    def _execute(self, query):
        """ execute query """

        # connect to db

        with self._connect() as conn:

            # getting connection object
            cur = conn.cursor()

            logger.debug("Execute query:")
            logger.debug(query)
            logger.debug(conn.__dict__)

            try:

                # execute & commit query
                cur.execute(query)
                conn.commit()

                # return last_id
                return int(cur.lastrowid)

            except Exception as e:
                # rollback if error
                conn.rollback()
                logger.error(query)
                logger.error(e)

        return -1

    def _connect(self):
        """ return connection to database """
        vars = self.ssh_tunnel_info.copy()
        vars.update(self.mysql_auth_info)
        return MysqlTunnelConnection(**vars)

    def _toJson(self, desc, _tuple):
        """ tuple from select query to json """
        f = lambda x: int(x) if type(x) in [long, int] else x
        _tuple = [f(val) for val in _tuple ]

        return dict(zip([_desc[0] for _desc in desc], _tuple))