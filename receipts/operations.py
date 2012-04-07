# -*- coding: utf-8 -*-

"""
Operations supported by ``receipts``.
"""

from receipts.core_types import Receipt


def add_receipt(**kwargs):
    """Add a receipt to the database."""
    vat = kwargs['vat']
    price = kwargs['price']
    when = kwargs['when']
    Receipt(vat, price, when).save()


def report_month(**kwargs):
    """Show a report for the specified month."""
    month = kwargs['month']
    print(month)
