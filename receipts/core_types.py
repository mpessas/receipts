# -*- coding: utf-8 -*-

"""
Available data types.
"""

import re
from decimal import Decimal, Context, ROUND_HALF_UP, InvalidOperation
from datetime import date
import sqlite3


class Vat(object):
    """VAT Registration Number type."""

    _regex = re.compile(r'\d{9}$')

    def __init__(self, vat):
        self._validate(vat)
        self._vat = vat

    @classmethod
    def _validate(self, vat):
        """Validate a VAT number.

        A VAT must have 9 digits.

        :params vat: A VAT number to validate against.
        :raises: TypeError, in case of a wrong VAT format.
        """
        if self._regex.match(vat) is None:
            raise TypeError("Wrong VAT number: %s" % vat)

    def __conform__(self, protocol):
        """Convert to SQLite."""
        if protocol is sqlite3.PrepareProtocol:
            return "%s" % self._vat

    def __str__(self):
        return "%s" % self._vat


class Price(object):
    """Price type."""

    _context = Context(prec=2, rounding=ROUND_HALF_UP, Emin=-2)

    def __init__(self, price):
        try:
            self._price = Decimal(price, context=self._context)
        except InvalidOperation as e:
            raise TypeError("Invalid price format: %s" % price)
        self._validate(self._price)

    @classmethod
    def _validate(self, price):
        if price <= 0:
            raise TypeError("Negative price given: %s" % price)

    def __conform__(self, protocol):
        """Convert to SQLite."""
        if protocol is sqlite3.PrepareProtocol:
            return "%s" % self._price

    def __str__(self):
        return '%s €' % self._price


class Receipt(object):
    """Receipt type."""

    def __init__(self, vat, price, date):
        self._vat = Vat(vat)
        self.price = Price(price)
        self.date = Date(date)
