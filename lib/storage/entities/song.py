from .entity import Entity
import equalizer.config as app

class Song(Entity):
    _table = app.SONG_TABLE
    _pk = app.SONG_TABLE_PK
    _existsQuery = app.SONG_EXISTS_QUERY

    def __init__(self, song_id = 0, song_title = None, country = None, genre = None,
                 release_date = None, itunes_song_id = None, duration = None, **kwargs):
        self.song_id = song_id
        self.song_title = song_title
        self.duration = duration
        self.country = country
        self.genre = genre
        self.release_date = release_date
        self.itunes_song_id = itunes_song_id