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

from abstract_attribute import AbstractAttribute
from equalizer.lib.data.parsers import IntegerParser

class IntegerAttribute(AbstractAttribute):
    """ integer attribute object """

    def __init__(self, key, value):
        try:
            value = IntegerParser().parse(value)
        except:
            if not isinstance(value, int) and \
                    not isinstance(value, long) and value != None:
                raise TypeError("PrimaryKey value must be of type int/long")
        super(IntegerAttribute, self).__init__(key, value)

    @overrides
    def __repr__(self):
        """ return value representation for mysql query """
        return IntegerParser().toStr(self.value())
