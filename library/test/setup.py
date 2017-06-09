#!/usr/bin/env python

try:
    from setuptools import setup, find_packages, Extension
except ImportError:
    from distutils.core import setup, find_packages, Extension

setup(
    name            = 'Rainbow Hat',
    version         = '1.0.0',
    author          = 'sudeep',
    author_email    = 'sudeepalloblr@gmail.com',
    url             = '',
    description     = """Python library for Rainbow HAT""",
    long_description=open('README.txt').read() + open('CHANGELOG.txt').read(),
    py_modules      = [ 'RainbowHat' ]
)
