from .entity import Entity
import equalizer.config as app

class ArtistSong(Entity):
    _table = app.ARTIST_SONG_TABLE
    _pk = app.ARTIST_SONG_TABLE_PK
    _existsQuery = app.ARTIST_SONG_EXISTS_QUERY

    def __init__(self, artist_song_id = 0, artist_id = None,
                 song_id = None, **kwargs):
        self.artist_song_id = artist_song_id
        self.artist_id = artist_id
        self.song_id = song_id