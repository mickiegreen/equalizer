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