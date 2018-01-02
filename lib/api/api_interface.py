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

""" Adapter for api implementation """
class Api(object):
    def get(self):
        """ call api """
        raise NotImplementedError

    def info(self):
        """ get api params (target url, params) as json """
        raise NotImplementedError

    def json(self):
        """ call api and convert to json """
        raise NotImplementedError

    def set(self, key, val):
        """ set parameter """
        raise NotImplementedError

    def set_url(self, url):
        """ set api url """
        raise NotImplementedError

    def get_url(self):
        """ return the basic url of the request """
        raise NotImplementedError

    def get_full_url(self):
        """ return the full url generated for the api """
        raise NotImplementedError
