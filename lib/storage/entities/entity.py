class Entity(object):
    _table = 'untitled'
    _pk = '_pk_unset'
    _existsQuery = {'query' : '', 'keys' : ''}

    def __init__(self, **kwargs):
        raise NotImplementedError

    def table(self):
        return self._table

    def toMySQL(self):
        cols = [k for k in self.json().keys()]
        vals = [str(self.json()[k]) for k in cols if self.json()[k] != None]

        return cols, vals

    def json(self):
        return self.__dict__.copy()

    def update(self, **kwargs):
        if kwargs.get(self._pk) != self._pk:
            raise ValueError("cannot override object primary key")

        self.__init__(**kwargs)

    def existsQuery(self):
        return self._existsQuery.get('query','') %self.__existsQueryKeys()

    def __existsQueryKeys(self):
        keys = self._existsQuery.get('keys',[])
        return tuple(str(getattr(self, key)) for key in keys)

    def get_primary_key(self):
        return (self._pk, getattr(self, self._pk))

    def set_primary_key(self, primary_key):
        setattr(self, self._pk, primary_key)

    def copy(self):
        return self.__class__(**self.json())

    def upgrade(self, record):
        """ assuming record is the new updated object """
        k, v = record.get_primary_key()
        if v != self.get_primary_key()[1]:
            raise ValueError("object must have the same primary key")

        for k, v in record.json().items():
            if v != None:
                setattr(self, k, v)

    def __eq__(self, other):
        if not isinstance(self.__class__, other):
            return False

        for k,v in other.json().items():
            if self.json().get(k, None) != v: return False

        return True

    def __repr__(self):
        return self.json().__repr__()
