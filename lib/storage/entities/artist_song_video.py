from .entity import Entity

import equalizer.config as app

class ArtistSongVideo(Entity):
    _table = app.ARTIST_SONG_VIDEO_TABLE
    _pk = app.ARTIST_SONG_VIDEO_TABLE_PK
    _existsQuery = app.ARTIST_SONG_VIDEO_EXISTS_QUERY

    def __init__(self, artist_song_video_id = 0,
                 artist_song_id = None, video_id = None, **kwargs):
        self.artist_song_video_id = artist_song_video_id
        self.artist_song_id = artist_song_id
        self.video_id = video_id
