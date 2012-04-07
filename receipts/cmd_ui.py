# -*- coding: utf-8 -*-

import argparse
from datetime import date
from receipts.info import description


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


def setup_parser():
    """
    Setup the cmd parser.
    """
    parser = argparse.ArgumentParser(description=description)
    subparsers = parser.add_subparsers()

    # Parser for the add command.
    parser_add = subparsers.add_parser('add', help="Add a new receipt.")
    parser_add.add_argument('vat', help="The VAT number", metavar='VAT')
    parser_add.add_argument('price', help="The price")
    parser_add.add_argument('when', help="The date", metavar='date')
    parser_add.set_defaults(func=add_receipt)

    # Parser for the report command.
    parser_report = subparsers.add_parser('report', help="Show a report.")
    parser_report.add_argument(
        '-m', '--month', default=date.today().month,
        choices=list(range(1, 13)), type=int
    )
    parser_report.set_defaults(func=report_month)

    return parser
