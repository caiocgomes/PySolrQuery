#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
long_description = f.read()
f.close()

setup(
    name='pySolrQuery',
    version=0.0.1,
    description='Python API for Solr queries',
    long_description=long_description,
    url='http://github.com/rcalsaverini/PySolrQuery',
    author='Rafael S. Calsaverini',
    author_email='rafael.calsaverini(at)gmail(dot)com',
    keywords=['Solr', 'search'],
    license='Public Domain',
    packages = find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        ]
)
