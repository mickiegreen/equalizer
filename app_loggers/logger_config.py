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
#           LOGGING            #
#                              #
#******************************#

import sys
import logging
from logging import handlers

LOG_FILE_NAME = 'equalizer.log'
LOGGER_CONFIG = False
LOGGING_LEVEL = 'INFO'

__loggers = {}

def __set_logger():
    # TODO put logging configurations in __hidden
    formatter = logging.Formatter(
        '\n'
        'TIME    :: [%(asctime)s,%(msecs)d]\n'
        'FILE    :: [<%(filename)s> at line <%(lineno)d>]\n'
        'LEVEL   :: [%(levelname)s]\n'
        'MESSAGE :: %(message)s'
    )
    logging.basicConfig(filename=LOG_FILE_NAME,
             filemode='a',
             datefmt='%H:%M:%S',
             level=LOGGING_LEVEL)
    logger = logging.getLogger(LOG_FILE_NAME)
    if not logger.handlers:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        fh = handlers.RotatingFileHandler(LOG_FILE_NAME, maxBytes=(104857), backupCount=7)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    __loggers['logger'] = logging.getLogger(LOG_FILE_NAME)

if len(__loggers) == 0:
    __set_logger()

LOGGER = __loggers['logger']