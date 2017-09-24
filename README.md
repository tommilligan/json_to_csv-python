# json_to_csv-python

[![Travis branch](https://img.shields.io/travis/tommilligan/json_to_csv-python/develop.svg)](https://travis-ci.org/tommilligan/json_to_csv-python)
[![codecov](https://codecov.io/gh/tommilligan/json_to_csv-python/branch/develop/graph/badge.svg)](https://codecov.io/gh/tommilligan/json_to_csv-python)
[![Requires.io](https://img.shields.io/requires/github/tommilligan/json_to_csv-python.svg)](https://requires.io/github/tommilligan/json_to_csv-python/requirements/?branch=master)
[![license](https://img.shields.io/github/license/tommilligan/json_to_csv-python.svg)]()


## Installation

Clone and install using pip
```bash
git clone git@github.com:tommilligan/json_to_csv-python
pip install ./json_to_csv-python
```

Any additional scripts in the `notes` folder require dev-dependencies


## Development

Install with
```
pip install -e ./json_to_csv-python
pip install -r requirements-dev.txt
```

Development tasks
```
# Test and cover
nose2 --with-coverage --coverage-report html
```
