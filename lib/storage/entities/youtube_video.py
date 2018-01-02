from .entity import Entity
import equalizer.config as app

class YoutubeVideo(Entity):
    _table = app.YOUTUBE_VIDEO_TABLE
    _pk = app.YOUTUBE_VIDEO_TABLE_PK
    _existsQuery = app.YOUTUBE_VIDEO_EXISTS_QUERY

    def __init__(self, video_id = 0, likes = None, comments = None,
            views = None, favorites = None, dislikes = None,
            youtube_video_id = 0, youtube_video_title = None, **kwargs):
        self.video_id = video_id
        self.likes = likes
        self.comments = comments
        self.views = views
        self.favorites = favorites
        self.dislikes = dislikes
        self.youtube_video_id = youtube_video_id
        self.youtube_video_title = youtube_video_title
