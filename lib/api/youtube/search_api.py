# -*- coding: utf-8 -*-

# Copyright (c) 2018 Michael Green
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from .. import BasicApi
from .__utils import app
import logging
logger = logging.getLogger()


class YoutubeSearchApi(BasicApi):

    def __init__(self, keywords = [], keys = []):
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
            logger.info(self.get_full_url())
            res = self.get()
            data = res['items']

            for video in data:
                video_data = {}

                for k in self.keys:
                    video_data[k] = video['snippet'].get(k, None)
                    if video_data[k] == None: video_data.pop(k)

                video_data['videoId'] = video['id']['videoId']

                videos.append(video_data)

        except:
            # TODO handle error
            pass

        return videos

