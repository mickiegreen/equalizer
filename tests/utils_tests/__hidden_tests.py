import unittest
import json

from lib.utils.__hidden import load_itunes_results, itunes_keywords, \
    itunes_to_youtube, records_to_mysql, load_full_records
from tests.tests_config import LOGGER as logger
from tests import tests_config as app

class TestHidden(unittest.TestCase):
    def setUp(self):
        pass

    @unittest.skip
    def test_load_itunes_results(self):
        results = load_itunes_results(limit = 20)
        logger.info("results-num : " + str(len(results)))
        logger.debug("first-result:")
        logger.debug(json.dumps(results[0]))

    @unittest.skip
    def test_itunes_keywords(self):
        keywords = '+'.join(itunes_keywords(app.TEST_ITUNES_KEYWORDS))
        if not keywords.__eq__(app.TEST_ITUNES_KEYWORDS_RESULTS):
            logger.error("TestHidden.test_itunes_keywords failed: " + keywords)

    def test_itunes_to_youtube(self):
        itunes = load_itunes_results(100000)[:1]
        itunes_to_youtube(itunes)
        logger.info("youtube results : check youtube folder")

    @unittest.skip
    def test_records_to_mysql(self):
        records = load_full_records(100000)
        import random
        random.shuffle(records)
        records_to_mysql(records)





