#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

sys.path.append('../src')
setup(
    name                = 'exchange',
    version             = '0.0.2',
    description         = 'Central control server for the smart learning system',
    packages            = find_packages('src'),
    package_dir         = {'':'src'},
    scripts             = ['src/__main__.py'],
     entry_points={
        'setuptools.installation': [
            'eggsecutable = src.__main__:main',
        ]
    },
    install_requires    = ['netdisco', 'pywemo'],
    test_suite          = 'nose.collector',
    tests_require       = ['nose'],
    zip_safe            = False,
    package_data        ={'':['*.config']}
)
