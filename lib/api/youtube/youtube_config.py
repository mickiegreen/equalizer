YOUTUBE_LIMIT = 200
YOUTUBE_VIDEO_URLS_LIMIT = 3
YOUTUBE_OVERRIDE = True

YOUTUBE_EMBED_URL = 'https://www.youtube.com/embed/%s'

YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
YOUTUBE_SEARCH_PARAMS = {'part' : 'snippet', 'type' : 'video', 'maxResults' : str(YOUTUBE_VIDEO_URLS_LIMIT)}


YOUTBUE_VIDEOS_URL = 'https://www.googleapis.com/youtube/v3/videos'

YOUTUBE_VIDEO_DETAILS_PARAMS = {'part' : 'contentDetails'}


YOUTUBE_VIDEO_PLAYER_PARAMS = {'part' : 'player'}


YOUTUBE_VIDEO_STATISTICS_PARAMS = {'part' : 'statistics'}
