TEST_YOUTUBE_TOKEN = 'AIzaSyATGzqdcCvkr_lV4ocVhagTKDCO6Ng-ods'
TEST_YOUTUBE_KEYWORDS = ['andy', 'williams', 'where', 'do', 'I', 'begin']

TEST_ITUNES_KEYWORDS = {
    "artist_name"       : "Lyrics Born",
    "release_date"      : "2008-04-19T07:00:00Z",
    "song_title"        : "I Like It, I Love It",
    "country"           : "BRA",
    "itunes_song_id"    : 277501238,
    "itunes_artist_id"  : 3083144,
    "genre"             : "Hip-Hop/Rap"
}

TEST_ITUNES_KEYWORDS_RESULTS = "Lyrics+Born+I+Like+It,+I+Love+It"

TEST_RECORDS_TO_MYSQL = [{'genre': 'Hip-Hop/Rap', 'views': '635410', 'youtube_video_id': 'BHgnuw10UuY', 'song_title': 'I Like It, I Love It', 'comments': '242', 'artist_song_video_id': 0, 'itunes_artist_id': 3083144, 'dislikes': '67', 'country': 'BRA', 'video_id': 0, 'favorites': '0', 'itunes_song_id': 277501238, 'release_date': '2008-04-19T07:00:00Z', 'song_id': 0, 'duration': 'PT3M43S', 'artist_song_id': 0, 'artist_name': 'Lyrics Born', 'likes': '2460', 'artist_id': 0}, {'genre': 'Hip-Hop/Rap', 'views': '298013', 'youtube_video_id': 'N9Wph7BnK78', 'song_title': 'I Like It, I Love It', 'comments': '139', 'artist_song_video_id': 0, 'itunes_artist_id': 3083144, 'dislikes': '46', 'country': 'BRA', 'video_id': 0, 'favorites': '0', 'itunes_song_id': 277501238, 'release_date': '2008-04-19T07:00:00Z', 'song_id': 0, 'duration': 'PT3M44S', 'artist_song_id': 0, 'artist_name': 'Lyrics Born', 'likes': '1516', 'artist_id': 0}, {'genre': 'Hip-Hop/Rap', 'views': '79603', 'youtube_video_id': '7wUSOEGOUGM', 'song_title': 'I Like It, I Love It', 'comments': '15', 'artist_song_video_id': 0, 'itunes_artist_id': 3083144, 'dislikes': '18', 'country': 'BRA', 'video_id': 0, 'favorites': '0', 'itunes_song_id': 277501238, 'release_date': '2008-04-19T07:00:00Z', 'song_id': 0, 'duration': 'PT3M45S', 'artist_song_id': 0, 'artist_name': 'Lyrics Born', 'likes': '239', 'artist_id': 0}, {'genre': 'R&B/Soul', 'views': '3623276', 'youtube_video_id': 'gmv54pfxk0Q', 'song_title': 'Every Night (alternate)', 'comments': '28', 'artist_song_video_id': 0, 'itunes_artist_id': 800878, 'dislikes': '1597', 'country': 'BRA', 'video_id': 0, 'favorites': '0', 'itunes_song_id': 407554855, 'release_date': '2010-11-15T08:00:00Z', 'song_id': 0, 'duration': 'PT0S', 'artist_song_id': 0, 'artist_name': 'Lyrics', 'likes': '47804', 'artist_id': 0}, {'genre': 'R&B/Soul', 'views': '3554954', 'youtube_video_id': '0nVvRwrgsGU', 'song_title': 'Every Night (alternate)', 'comments': '4132', 'artist_song_video_id': 0, 'itunes_artist_id': 800878, 'dislikes': '906', 'country': 'BRA', 'video_id': 0, 'favorites': '0', 'itunes_song_id': 407554855, 'release_date': '2010-11-15T08:00:00Z', 'song_id': 0, 'duration': 'PT2M57S', 'artist_song_id': 0, 'artist_name': 'Lyrics', 'likes': '26944', 'artist_id': 0}, {'genre': 'R&B/Soul', 'views': '25564', 'youtube_video_id': 'kkNp7MVjQ-I', 'song_title': 'Every Night (alternate)', 'comments': '7', 'artist_song_video_id': 0, 'itunes_artist_id': 800878, 'dislikes': '18', 'country': 'BRA', 'video_id': 0, 'favorites': '0', 'itunes_song_id': 407554855, 'release_date': '2010-11-15T08:00:00Z', 'song_id': 0, 'duration': 'PT2M58S', 'artist_song_id': 0, 'artist_name': 'Lyrics', 'likes': '228', 'artist_id': 0}]


#******************************#
#                              #
#           LOGGING            #
#                              #
#******************************#
'''import logging

LOG_FILE_NAME = 'unittests.log'
LOGGER_CONFIG = True
LOGGING_LEVEL = logging.DEBUG

def __set_logger():
    import sys
    logging.basicConfig(filename=LOG_FILE_NAME,
             filemode='a',
             format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
             datefmt='%H:%M:%S',
             level=LOGGING_LEVEL)
    logger = logging.getLogger()
    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)

if LOGGER_CONFIG:
    __set_logger()

LOGGER = logging.getLogger()'''


# from equalizer.config import LOGGER





