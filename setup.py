#!/usr/bin/env python
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def readfile(fname):
    fh = open(os.path.join(os.path.dirname(__file__), fname))
    contents = fh.readlines()
    fh.close()
    return contents

long_description = '\n'.join(readfile('README.md'))
requirements = readfile('requirements.txt')


setup(
    name='pySolrQuery',
    version='0.0.1',
    description='Python API for Solr queries',
    long_description=long_description,
    url='http://github.com/rcalsaverini/PySolrQuery',
    author='Rafael S. Calsaverini',
    author_email='rafael.calsaverini(at)gmail(dot)com',
    keywords=['Solr', 'search'],
    license='Public Domain',
    install_requires = requirements,
    classifiers=[
        'Intended Audience :: Developers',
        ]
)
