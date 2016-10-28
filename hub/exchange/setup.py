#!/usr/bin/env python3

from setuptools import setup

setup(
    name                = 'ctrl-serve',
    version             = '0.0.1',
    description         = 'Central control server for the smart learning system',
    install_requires    = [

    ],
    test_suite          = 'nose.collector',
    tests_require       = [
        'nose'
    ],
    zip_safe = False
)
