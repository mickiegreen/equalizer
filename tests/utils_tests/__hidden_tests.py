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

import unittest
import json
import random

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

    def test_itunes_keywords(self):
        keywords = '+'.join(itunes_keywords(app.TEST_ITUNES_KEYWORDS))
        if not keywords.__eq__(app.TEST_ITUNES_KEYWORDS_RESULTS):
            logger.error("TestHidden.test_itunes_keywords failed: " + keywords)

    def test_itunes_to_youtube(self):
        itunes = load_itunes_results(100000)
        random.shuffle(itunes)
        end = len(itunes) if len(itunes) <= 30000 else 30000
        itunes_to_youtube(itunes[:end])
        logger.info("youtube results : check youtube folder")

    @unittest.skip
    def test_records_to_mysql(self):
        records = load_full_records(100000)
        random.shuffle(records)
        records_to_mysql(records)





