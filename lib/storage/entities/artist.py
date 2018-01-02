from .entity import Entity
import equalizer.config as app

class Artist(Entity):
    _table = app.ARTIST_TABLE
    _pk = app.ARTIST_TABLE_PK
    _existsQuery = app.ARTIST_EXISTS_QUERY

    def __init__(self, artist_id = 0, artist_name = None, itunes_artist_id = None, **kwargs):
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.itunes_artist_id = itunes_artist_id
