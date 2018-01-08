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

from overrides import overrides
import datetime

from .parser_interface import ParserInterface

class DurationParser(ParserInterface):
    """
    Adapter to parse duration in milliseconds (timestamp)
    to timedelta object
    """

    @overrides
    def parse(self, value):
        """ implement parsing logic here """

        if type(value) == str:
            value = datetime.datetime.strptime(value, '%H:%M:%S')

        # convert to format
        _time = datetime.datetime.fromtimestamp(value / 1000.0).time()
        value = _time.strftime('%H:%M:%S')
        value = datetime.datetime.strptime(value, '%H:%M:%S').time()
        return value

    def toStr(self, value):
        """ return value as str to fit mysql query """

        if type(value) == str:
            value = datetime.datetime.strptime(value, '%H:%M:%S').time()

        elif type(value) == datetime.timedelta:
            value = datetime.datetime.strptime(str(value), '%H:%M:%S').time()

        # make compatible with queries structure
        return "'" + datetime.time.strftime(value, '%H:%M:%S') + "'"
