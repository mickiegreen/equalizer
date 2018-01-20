from ..basic_api import BasicApi
from .__utils import app

class VideoDetailsApi(BasicApi):
    def __init__(self, video_id, keys = []):
        params = app.YOUTUBE_VIDEO_DETAILS_PARAMS.copy()
        params['id'] = video_id

        super(VideoDetailsApi, self).__init__(
            url = app.YOUTBUE_VIDEOS_URL,
            params = params
        )
        self.keys = keys

    def json(self):
        details = {}

        try:
            res = self.get()
            data = res.get('items', [])

            for video in data:
                for k in self.keys:
                    contentDetails = video['contentDetails']
                    details[k] = contentDetails.get(k, None)
                    if details[k] == None: details.pop(k)
                details['videoId'] = video['id']

        except Exception as e:
            print(e)

        return details
