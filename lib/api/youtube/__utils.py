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

import os
import json

TOKEN_FOLDER = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
TOKEN_FILE = TOKEN_FOLDER + os.sep + 'token.json'

def __load_token():
    with open(TOKEN_FILE, 'r') as _f:
        return json.load(_f)['key']

def __load_config():
    from . import youtube_config as app

    YOUTUBE_TOKEN = __load_token()
    app.YOUTUBE_SEARCH_PARAMS['key'] = YOUTUBE_TOKEN
    app.YOUTUBE_VIDEO_DETAILS_PARAMS['key'] = YOUTUBE_TOKEN
    app.YOUTUBE_VIDEO_PLAYER_PARAMS['key'] = YOUTUBE_TOKEN
    app.YOUTUBE_VIDEO_STATISTICS_PARAMS['key'] = YOUTUBE_TOKEN

    return app

app = __load_config()