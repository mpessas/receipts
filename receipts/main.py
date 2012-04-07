# -*- coding: utf-8 -*-

import sys
import receipts.settings
import receipts.db
from receipts.core_types import Receipt
from receipts.cmd_ui import setup_parser, add_receipt, report_month


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = setup_parser()
    args = parser.parse_args(argv)
    args.func(**vars(args))
    return 0


if __name__ == '__main__':
    sys.exit(main())
