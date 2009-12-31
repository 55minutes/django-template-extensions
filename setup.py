#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


DISTRIBUTION_NAME = '55M-Django-Template-Extensions'

SHORT_DESCRIPTION = 'Useful Django template tags and filters'
if os.path.exists("README.rst"):
    LONG_DESCRIPTION = codecs.open("README.rst", "r", "utf-8").read()
else:
    LONG_DESCRIPTION = SHORT_DESCRIPTION

PACKAGE_URL = 'https://internal.55minutes.com/svn/fiftyfive/python/trunk/django/apps/55-template-extensions/'


setup(
    name=DISTRIBUTION_NAME,
    version='1.0',
    author='55 Minutes',
    author_email='info@55minutes.com',
    maintainer='55 Minutes',
    maintainer_email='info@55minutes.com',
    url=PACKAGE_URL,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    download_url=PACKAGE_URL,
    platforms=["any"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Programming Language :: Python",
    ],
    license="All Rights Reserved (c) 2010 55 Minutes",

    package_dir = {'':'src'},
    packages=find_packages('src'),
    zip_safe=False,
    include_package_data=True,
)
