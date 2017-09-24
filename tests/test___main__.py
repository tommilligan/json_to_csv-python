#!/usr/bin/env python

import unittest

import json_to_csv.__main__ as subject

class TestMainParser(unittest.TestCase):
    def test_parser_compiles(self):
        subject.mainParser()
