class StorageEngine(object):
    def add(self, record):
        """add new record to relation"""
        raise NotImplementedError

    def remove(self, relation, id_key, id_val):
        """remove record from relation"""
        raise NotImplementedError

    def update(self, record):
        """update record in relation"""
        raise NotImplementedError

    def live_update(self, relation, override = True):
        """add more records to relation"""
        raise NotImplementedError