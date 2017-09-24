#!/usr/bin/env python

import io
import unittest

import json_to_csv as subject

# Test helpers

def assertDictSubset(self, subset, superset):
    """
    Additional method for ``unitest.TestCase`` to check dictionary subsetting

    :param self: unittest.TestCase
    :param dict subset:
    :param dict superset:
    """
    if not set(subset.items()).issubset(set(superset.items())):
        raise AssertionError("{0} is not subset of {1}".format(subset, superset))

class TestAssertDictSubset(unittest.TestCase):
    def setUp(self):
        self.superset = {"spam": "ham", "foo": "bar"}

    def test_subset(self):
        subset = {"spam": "ham"}
        assertDictSubset(self, subset, self.superset)

    def test_subset_invalid_value(self):
        subset = {"spam": "eels"}
        with self.assertRaises(AssertionError):
            assertDictSubset(self, subset, self.superset)

    def test_subset_invalid_key(self):
        subset = {"hovercraft": "ham"}
        with self.assertRaises(AssertionError):
            assertDictSubset(self, subset, self.superset)

    def test_superset(self):
        subset = {"spam": "ham", "foo": "bar", "mother": "hamster"}
        with self.assertRaises(AssertionError):
            assertDictSubset(self, subset, self.superset)


class TestStructureToRelationalDicts(unittest.TestCase):
    def test_string(self):
        testInput = "spam"
        expected = [
            {
                "type": "str",
                "value": "spam"
            }
        ]
        actual = subject.structureToRelationalDicts(testInput)
        for a, e in zip(actual, expected):
            assertDictSubset(self, e, a)

    def test_stringable(self):
        testInput = 3.14159
        expected = [
            {
                "type": "str",
                "value": "3.14159"
            }
        ]
        actual = subject.structureToRelationalDicts(testInput)
        for a, e in zip(actual, expected):
            assertDictSubset(self, e, a)

    def test_bool(self):
        testInput = True
        expected = [
            {
                "type": "bool",
                "value": "TRUE"
            }
        ]
        actual = subject.structureToRelationalDicts(testInput)
        for a, e in zip(actual, expected):
            assertDictSubset(self, e, a)

    def test_none(self):
        testInput = None
        expected = [
            {
                "type": "null",
                "value": "NULL"
            }
        ]
        actual = subject.structureToRelationalDicts(testInput)
        for a, e in zip(actual, expected):
            assertDictSubset(self, e, a)

    def test_dict(self):
        testInput = {
            "foo": "bar"
        }
        expected = [
            {
                "type": "str",
                "value": "bar",
                "key": "foo"
            },
            {
                "type": "dict",
                "value": None,
                "key": None
            }
        ]
        actual = subject.structureToRelationalDicts(testInput)
        for a, e in zip(actual, expected):
            assertDictSubset(self, e, a)

    def test_list(self):
        testInput = [
            "rabbit"
        ]
        expected = [
            {
                "type": "str",
                "value": "rabbit",
                "key": "0"
            },
            {
                "type": "list",
                "value": None,
                "key": None
            }
        ]
        actual = subject.structureToRelationalDicts(testInput)
        for a, e in zip(actual, expected):
            assertDictSubset(self, e, a)

    def test_nested(self):
        testInput = {
            "qux": [
                {
                    "number": 42
                },
                {
                    "number": 0
                }
            ]
        }
        expected = [
            {
                "type": "str",
                "value": "42",
                "key": "number"
            },
            {
                "type": "dict",
                "value": None,
                "key": "0"
            },
            {
                "type": "str",
                "value": "0",
                "key": "number"
            },
            {
                "type": "dict",
                "value": None,
                "key": "1"
            },
            {
                "type": "list",
                "value": None,
                "key": "qux"
            },
            {
                "type": "dict",
                "value": None,
                "key": None
            }
        ]
        actual = subject.structureToRelationalDicts(testInput)
        for a, e in zip(actual, expected):
            assertDictSubset(self, e, a)

