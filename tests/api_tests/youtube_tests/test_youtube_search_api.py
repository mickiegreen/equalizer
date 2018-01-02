import unittest
import json

from equalizer.lib.api.youtube import add_token, YoutubeSearchApi
from equalizer.tests.tests_config import LOGGER as logger
from equalizer.tests import tests_config as config

class TestYoutubeSearchApi(unittest.TestCase):
    """ testing youtube search api """

    def setUp(self):
        """ setting up token to youtube module """
        self.token = config.TEST_YOUTUBE_TOKEN
        self.keywords = config.TEST_YOUTUBE_KEYWORDS
        add_token(self.token)
        logger.info("set token - " + self.token)

    def test_json(self):
        """ checking if got videos with proper structure """
        res = YoutubeSearchApi(*self.keywords).json()

        if len(res) < 1:
            logger.error('TestYoutubeSearchApi.test_json - no results')

        else :
            logger.info(json.dumps(res, indent=4, sort_keys=True))
