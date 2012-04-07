# -*- coding: utf-8 -*-

"""
Logging functions and data.
"""

import sys
import logging
from receipts.settings import LOG_LEVEL


class _InteractiveFilter(logging.Filter):
    """
    Filter for interactive messages.
    """

    def filter(self, record):
        if record.levelno >= logging.WARNING:
            return 0
        return 1


logger = logging.getLogger('receipts')
logger.setLevel(getattr(logging, LOG_LEVEL))
_format = logging.Formatter(fmt='%(message)s')

_out_handler = logging.StreamHandler(stream=sys.stdout)
_out_handler.setFormatter(_format)
_out_handler.setLevel(logging.DEBUG)
_out_handler.addFilter(_InteractiveFilter())

_err_handler = logging.StreamHandler()
_err_handler.setFormatter(_format)
_err_handler.setLevel(logging.WARNING)

logger.addHandler(_out_handler)
logger.addHandler(_err_handler)
