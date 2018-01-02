import pymysql as MySQLdb

from .storage_engine import StorageEngine

class MySqlEngine(StorageEngine):
    def __init__(self, host, user, password, schema, port = 3306):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.schema = schema

    def add(self, record):
        # TODO force entity type
        cols, vals = record.toMySQL()
        relation = record.table()

        with self.__connect() as cur:
            conn = cur.connection

            try:
                query = "INSERT INTO %s (%s) VALUES (%s)" %(relation, ','.join(cols), ','.join(vals))

                print(query)

                # add row to table
                cur.execute(query)
                conn.commit()

                # update record to new id
                record_id = cur.lastrowid
                record.set_primary_key(record_id)

            except Exception as e:
                # print error
                conn.rollback()
                print('error', e, record.table())

                # set id to error id
                record_id = -1
                record.set_primary_key(record_id)

        return record_id

    def get(self, record):
        # TODO force entity type

        with self.__connect() as cur:
            conn = cur.connection

            try:
                # setting query to fetch as key
                query = record.existsQuery()

                print(query)

                # get row
                count = conn.query(query)

                if count > 0:
                    cur.execute(query)
                    row = self.__tuple_to_json(cur.fetchone(), cur.description)
                    record.update(**row)

                    _pk, record_id = record.get_primary_key()

                else:
                    return -1

            except Exception as e:
                # print error
                print('error', e, record.table())

                # set id to error id
                record_id = -1

        return record_id

    def __json(self, cur):
        pass

    def add_all(self, records):
        # TODO force entity type

        with self.__connect() as cur:
            conn = cur.connection

            try:
                # add all rows to table
                for record in records:
                    cols, vals = record.toMySQL()
                    relation = record.table()

                    cur.execute("INSERT INTO %s (%s) VALUES (%s)",
                            (relation, ','.join(cols), ','.join(vals)))

                    record_id = cur.lastrowid
                    record.set_primary_key(record_id)

                # commit all
                conn.commit()
            except:
                conn.rollback()

    def remove(self, relation, id_key, id_val):
        with self.__connect() as conn:
            cur = conn.cursor()
            try:
                delstatmt = "DELETE FROM %s WHERE %s = ?" %relation
                cur.execute(delstatmt, (id_key, id_val))
                conn.commit()
            except:
                # TODO print massage error
                conn.rollback()

    def update(self, record):
        # TODO force entity type

        id_key, id_val = record.get_primary_key()
        values = ','.join([k+"='"+str(v) + "'" for k,v in record.json().items() if k != id_key])
        relation = record.table()

        with self.__connect() as conn:
            cur = conn.cursor()
            try:
                cur.execute('UPDATE %s SET %s WHERE %s=%d', (relation, values, id_key, id_val,))
                conn.commit()
            except:
                # TODO print massage error
                conn.rollback()

    def execute(self, query):
        with self.__connect() as conn:
            cur = conn.cursor()
            try:
                cur.execute(query)
                conn.commit()
            except:
                # TODO print massage error
                conn.rollback()

    def live_update(self, relation, override = True):
        """add more records to relation"""
        raise NotImplementedError

    def exists(self, record):
        """check if record exists in db"""
        return self.get(record) != -1

    def add_if_not_exist(self, record):
        """ check if record exists, if not add it """
        record_id = self.get(record.copy())
        if record_id == -1:
            self.add(record)
        else: record.set_primary_key(record_id)

        return record_id

    def update_if_exists_else_add(self, record):
        cur_record = record.copy()
        print('cur_record',cur_record)
        record_id = self.get(cur_record)
        if record_id != -1:
            record.set_primary_key(record_id)
            self.update(record)

        else:
            record_id = self.add(record)

        return record_id

    def __connect(self):
        return MySQLdb.connect(
                host = self.host,
                user = self.user,
                passwd = self.password,
                db = self.schema,
                port = self.port
        )

    def __tuple_to_json(self, tuple, description):
        keys = [_desc[0] for _desc in description]
        return dict(zip(keys, tuple))

