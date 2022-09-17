#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def read_file(file_path):
    with open(file_path, encoding='utf-8') as f:
        return f.read()


DIR_PATH = os.path.dirname(__file__)


setup(
    name='timesince',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'timesince=timesince.main:main'
        ],
    },
    install_requires=[],
    author='Mursalin',
    author_email='m@mail.com',
    url='',
    description='A simple and flexible date time to relative time converting library',
    long_description=read_file(os.path.join(DIR_PATH, 'README.md')),
    long_description_content_type='text/markdown',
    license=read_file(os.path.join(DIR_PATH, 'LICENSE')),
    keywords=[],
    classifiers=[
        'Development Status :: Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Topic :: Education',
        'Topic :: Software Development',
    ],
)