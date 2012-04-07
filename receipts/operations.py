# -*- coding: utf-8 -*-

"""
Operations supported by ``receipts``.
"""


def add_receipt(**kwargs):
    """Add a receipt to the database."""
    vat = kwargs['vat']
    price = kwargs['price']
    when = kwargs['when']
    print(vat, price, when)


def report_month(**kwargs):
    """Show a report for the specified month."""
    month = kwargs['month']
    print(month)
