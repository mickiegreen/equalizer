import json

from .search_api import YoutubeSearchApi
from .video_statistics_api import VideoStatisticsApi
from .video_details_api import VideoDetailsApi

from .__utils import TOKEN_FILE, __load_token

def token():
    try:
        __load_token()
    except:
        raise RuntimeError("Token isn't set yet. Call youtube.add_token")

def add_token(token):
    with open(TOKEN_FILE,'w') as _f:
        _f.write(json.dumps({'key' : token}))

def get(video_id, keys = []):
    video = VideoDetailsApi(video_id = video_id, keys = keys).json()
    video.update(VideoStatisticsApi(video_id = video_id, keys = keys).json())

    return video

def search(keywords, keys = []):
    return YoutubeSearchApi(keywords = keywords, keys = keys).json()