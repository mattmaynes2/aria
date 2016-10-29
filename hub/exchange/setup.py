#!/usr/bin/env python3

import sys
from setuptools import setup

sys.path.append('../src')
setup(
    name                = 'exchange',
    version             = '0.0.2',
    description         = 'Central control server for the smart learning system',
    install_requires    = [],
    test_suite          = 'nose.collector',
    tests_require       = ['nose'],
    zip_safe            = False
)
