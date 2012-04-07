# -*- coding: utf-8 -*-

import unittest
from itertools import chain
import sqlite3
from decimal import Decimal
from receipts.core_types import Vat, Price, Receipt
from receipts.db import conn


class VatTests(unittest.TestCase):
    """Tests for ``Vat`` type."""

    @classmethod
    def setUpClass(cls):
        cls.wrong_vats = ['01234', '0123456789', 'a', '012345678a']
        cls.correct_vats = ['012345678', '123456789', ]

    def test_validation(self):
        """Test VAT number validation."""
        for number in self.wrong_vats:
            self.assertRaises(TypeError, Vat._validate, number)
        for number in self.correct_vats:
            Vat._validate(number)

    def test_initializer(self):
        """Test initializer."""
        for number in self.wrong_vats:
            self.assertRaises(TypeError, Vat.__init__, number)
        for number in self.correct_vats:
            vat = Vat(number)
            self.assertEqual(vat._vat, number)


class PriceTests(unittest.TestCase):
    """Tests for the ``Price`` type."""

    @classmethod
    def setUpClass(cls):
        cls.negative_prices = ['-1234.23', ]
        cls.invalid_prices = ['12a.34', '12,34', ]
        cls.wrong_prices = chain(cls.negative_prices, cls.invalid_prices)
        cls.correct_prices = ['123.34', '0.1234', ]

    def test_validation(self):
        """Test price validation."""
        for price in self.negative_prices:
            self.assertRaises(TypeError, Price._validate, Decimal(price))
        for price in self.correct_prices:
            Price._validate(Decimal(price))

    def test_initializer(self):
        """Test the initialzier."""
        for price in self.wrong_prices:
            self.assertRaises(TypeError, Price.__init__, price)
        for price in self.correct_prices:
            p = Price(price)

    def test_sqlite_serializer(self):
        """Test conversion to sqlite3 data type."""
        for price in self.correct_prices:
            p = Price(price)
            self.assertEqual(p.__conform__(sqlite3.PrepareProtocol), price)


class ReceiptTests(unittest.TestCase):
    """Test the Receipt class."""

    def setUp(self):
        conn._filename = ":memory:"

    def tearDown(self):
        conn._reset_filename()

    def test_save_receipt(self):
        """Test saving a receipt."""
        r = Receipt('000000000', '10.23', '2012-03-12')
        r.save()
