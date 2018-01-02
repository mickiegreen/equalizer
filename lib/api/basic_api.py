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

import requests

from .api_interface import Api

class BasicApi(Api):
    """ basic api request adapter """

    def __init__(self, url, params):
        """ wrapping request object """
        self.__request = requests.Request(url = url, params = params, method = 'GET')

    def get(self):
        # prepare request object
        req = self.__request.prepare()

        # sending request
        with requests.Session() as session:
            return session.send(req).json()

    def info(self):
        return self.__dict__.copy()

    def set(self, key, val):
        """ setting get request parameters """
        self.__request.params[key] = val

    def set_url(self, url):
        self.__request.url = url

    def get_url(self):
        return self.__request.url

    def get_full_url(self):
        return self.__request.prepare().url
