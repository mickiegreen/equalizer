from .entity import Entity

class Collection(Entity):
    _table = 'collection'
    __pk = 'collection_id'

    def __init__(self, collection_id, collection_name, itunes_collection_id):
        self.collection_id = collection_id
        self.collection_name = collection_name
        self.itunes_collection_id = itunes_collection_id