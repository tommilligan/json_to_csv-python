#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="json_to_csv",
    version="0.1.0",
    license="Apache License 2.0",
    url="https://github.com/tommilligan/json_to_csv-python/",
    author="Tom Milligan",
    author_email="code@tommilligan.net",
    description="Convert json files to csv representation",
    keywords="json csv data convert transform",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    zip_safe=False,
    platforms="any",
    install_requires=[
    ],
    tests_require=[
        "nose2"
    ],
    test_suite="nose2.collector.collector",
    entry_points={
        "console_scripts": [
            "json_to_csv = json_to_csv.__main__:main"
        ]
    },
)