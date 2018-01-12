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

#******************************#
#                              #
#           SSH Server         #
#                              #
#******************************#
SSH_HOST = 'localhost'
SSH_PORT = '22'
SSH_USER = ''
SSH_PASSWORD = ''

#******************************#
#                              #
#             MySQL            #
#                              #
#******************************#
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_SCHEMA = ''
MYSQL_USER = ''
MYSQL_PASSWORD = ''

MYSQL_INFO = {
    'host'          : MYSQL_HOST,
    'port'          : MYSQL_PORT,
    'schema'        : MYSQL_SCHEMA,
    'user'          : MYSQL_USER,
    'password'      : MYSQL_PASSWORD
}

#******************************#
#                              #
#            Queries           #
#                              #
#******************************#

from database.queries import *

#******************************#
#                              #
#           LOGGING            #
#                              #
#******************************#

from app_loggers import LOGGER

try:
    from config_local import *
except:
    pass



