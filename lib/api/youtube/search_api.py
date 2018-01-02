from .. import BasicApi
from .__utils import app

class YoutubeSearchApi(BasicApi):

    def __init__(self, keywords = [], **keys):
        params = app.YOUTUBE_SEARCH_PARAMS.copy()

        if len(keywords) > 0:
            params['q'] = '+'.join(keywords)

        super(YoutubeSearchApi, self).__init__(
            url = app.YOUTUBE_SEARCH_URL,
            params = params
        )

        self.keys = keys

    def json(self):
        videos = []
        try:
            res = self.get()
            data = res['items']

            for video in data:
                video_data = {'youtube_video_id': video['id']['videoId']}

                for k,v in self.keys.items():
                    video_data[v] = video['snippet'].get(k, None)
                    if video_data[v] == None: video_data.pop(v)

                videos.append(video_data)

        except:
            # TODO handle error
            pass

        return videos

