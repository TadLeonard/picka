#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='picka',
    version='0.9',
    description='picka generates data for use in any application.',
    author='Anthony Long',
    author_email='antlong@gmail.com',
    packages=['picka'],
    include_package_data=True,
    package_data={'picka': ['*.sqlite', '*.txt']},
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python'],
    zip_safe=True,
    )
