from ..basic_api import BasicApi
from .__utils import app

class VideoDetailsApi(BasicApi):
    def __init__(self, video_id, **keys):
        params = app.YOUTUBE_VIDEO_DETAILS_PARAMS.copy()
        params['id'] = video_id

        super(VideoDetailsApi, self).__init__(
            url = app.YOUTBUE_VIDEOS_URL,
            params = params
        )
        self.keys = keys.get('keys')

    def json(self):
        details = {}

        try:
            res = self.get()
            data = res.get('items', [])

            for video in data:
                details['youtube_video_id'] = video['id']
                for k,v in self.keys.items():
                    contentDetails = video['contentDetails']
                    # TODO fix duration format
                    details[v] = contentDetails.get(k, None)
                    if details[v] == None: details.pop(v)

        except Exception as e:
            # TODO handle error
            print(e)

        return details
