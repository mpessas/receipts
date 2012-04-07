# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser


def init_settings(filename):
    config = ConfigParser()
    config.add_section('logging')
    config.set('logging', 'log_level', 'INFO')
    with open(filename, 'w') as f:
        config.write(f)


receipts_dir = os.path.expanduser('~/.receipts/')
if not os.path.exists(receipts_dir):
    os.mkdir(receipts_dir, 0o700)

settings_file = os.path.join(receipts_dir, 'receiptsrc')
if not os.path.exists(settings_file):
    init_settings(settings_file)

config = ConfigParser()
with open(settings_file, 'r') as f:
    config.readfp(f)

# Populate settings
LOG_LEVEL = config.get('logging', 'log_level')
