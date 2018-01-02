from ..basic_api import BasicApi
from .__utils import app

class VideoStatisticsApi(BasicApi):
    def __init__(self, video_id, **keys):
        params = app.YOUTUBE_VIDEO_STATISTICS_PARAMS.copy()
        params['id'] = video_id

        super(VideoStatisticsApi, self).__init__(
            url = app.YOUTBUE_VIDEOS_URL,
            params = params
        )

        self.keys = keys.get('keys')

    def json(self):
        statistics = {}

        try:
            res = self.get()
            data = res.get('items', [])

            for video in data:
                statistics['youtube_video_id'] = video['id']

                for k, v in self.keys.items():
                    statistics[v] = video['statistics'].get(k, None)
                    if statistics[v] == None: statistics.pop(v)

        except:
            # TODO handle error
            pass

        return statistics