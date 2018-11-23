#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://tmm-xmlrpc.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='tmm_xmlrpc',
    version='0.1.0',
    description='XMLRPC server for running TinyMediaManagerCMD',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Carlos "HurricaneHrndz" Hernandez',
    author_email='carlos@techbyte.ca',
    url='https://github.com/hurricanehrndz/tmm-xmlrpc',
    packages=[
        'tmm_xmlrpc',
    ],
    package_dir={'tmm_xmlrpc': 'tmm_xmlrpc'},
    include_package_data=True,
    scripts=['bin/tmm-xmlrpc'],
    install_requires=[
            ],
    license='MIT',
    zip_safe=False,
    keywords='tmm-xmlrpc',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
