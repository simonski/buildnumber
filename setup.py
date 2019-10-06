#!/usr/bin/env python
"""
https://packaging.python.org/en/latest/distributing.html
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
import os
from buildnumber import constants

here = path.abspath(path.dirname(__file__))

long_description = "A simple buildnumber generator."

setup(
    name="buildnumber",
    version=constants.VERSION,
    description="buildnumber is tool to control your build number.",
    long_description=long_description,
    url="https://github.com/simonski/buildnumber",
    author="Simon Gauld",
    author_email="simon.gauld@gmail.com",
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="buildnumber setuptools development",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["PyYAML==5.1.2"],
    test_suite="tests.test_suite",
    entry_points={"console_scripts": ["buildnumber=buildnumber:main"]},
)
