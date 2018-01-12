# -*- coding: utf-8 -*-

# Copyright (c) 2018 Karin Eliaz
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
import logging
logger = logging.getLogger()
import itunsed_config as app

class ItunesSearchApi(BasicApi):

    def __init__(self, country,term,releaseYearTerm):
        params = app.ITUNES_SEARCH_PARAMS.copy()

        params['country'] = country
        params['term'] = term
        params['releaseYearTerm'] = releaseYearTerm

        super(ItunesSearchApi, self).__init__(
            url = app.ITUNES_SEARCH_URL,
            params = params
        )


    def json(self):
        search_result = []
        logger.info(self.get_full_url())
        res = self.get()
        search_result=res.json()

        return search_result

