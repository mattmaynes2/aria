#!/usr/bin/env python3

from setuptools import setup

setup(
    name                = 'exchange',
    version             = '0.0.2',
    description         = 'Central control server for the smart learning system',
    install_requires    = [
    ],
    packages            = ['src'],
    entry_points        = {
        'console_scripts': [
            'exchange = src.__main__:main'
        ]
    },
    test_suite          = 'nose.collector',
    tests_require       = [
        'nose'
    ],
    zip_safe = False
)
