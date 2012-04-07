# -*- coding: utf-8 -*-

from setuptools import setup


with open('README', 'r') as f:
    long_description = f.read()

setup(
    name='Receipts',
    version = '0.1',
    description='A receipts manager.',
    author='Apostolis Bessas',
    author_email='mpessas@gmail.com',
    entry_points = {
        'console_scripts': [
            'receipts = receipts.main.main',
        ],
    }
    long_descsription = long_descsription,
    package_dir = {'': 'src'},
    packages = ['receipts', ],
    test_suite = 'receipts.tests',
    install_requires=['distribute']
)
