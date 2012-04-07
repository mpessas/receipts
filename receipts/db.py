# -*- coding: utf-8 -*-

"""
Database-related stuff.
"""

import os
import sqlite3
from receipts.settings import receipts_dir
from receipts.sql_queries import CREATE_TABLE_RECEIPTS, INSERT_RECEIPT


def _init_db(filename):
    with sqlite3.connect(filename) as conn:
        conn.execute(CREATE_TABLE_RECEIPTS)


class _Connection(object):
    """Connection object to a sqlite3 database."""

    _filename = os.path.join(receipts_dir, 'receipts.sqlite')

    def __init__(self):
        self._conn = None

    def __call__(self):
        """Get a connection object."""
        if self._conn is None:
            if not os.path.exists(self._filename):
                _init_db(self._filename)
            self._conn = sqlite3.connect(self._filename)
        return self._conn

    def _reset_filename(self):
        """Reset filename to the initial value."""
        self._filename = self.__class__._filename


conn = _Connection()


def insert_receipt(receipt):
    """Insert a receipt to the database."""
    with conn() as con:
        con.execute(INSERT_RECEIPT, receipt._db_values())
