#!/usr/bin/env python
"""
"""

import logging

def getModuleLogger(loggerName):
    """
    Returns a module logger. Call with::

        getModuleLogger(__name__)

    :param string loggerName:
    """
    newLogger = logging.getLogger(loggerName)
    newLogger.setLevel(logging.DEBUG)
    return newLogger