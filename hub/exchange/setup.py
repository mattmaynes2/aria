#!/usr/bin/env python3

import sys
from setuptools import setup, find_packages

sys.path.append('../src')
setup(
    name                = 'exchange',
    version             = '0.6.0',
    description         = 'Central control server for the smart learning system',
    packages            = find_packages('src'),
    package_dir         = { '':'src'},
    entry_points={
        'setuptools.installation': [
            'eggsecutable = src.__main__:main',
        ]
    },
    install_requires    = ['netdisco', 'pywemo','soco'],
    test_suite          = 'nose.collector',
    tests_require       = ['nose'],
    zip_safe            = False,
    package_data        ={'':['*.config', '*.sql']}
)
