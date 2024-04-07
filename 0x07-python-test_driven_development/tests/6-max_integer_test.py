#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]), None)

    def test_one_element(self):
        """Run unittest for a list with one element only"""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        """Tests a list of multiple positive integers only"""
        self.assertEqual(max_integer([5,10,15,12]), 15)

    def test_negative_numbers(self):
        """Tests a list of multiple negative integers only"""
        self.assertEqual(max_integer([-1, -10, -3]), -1)

    def test_mix_numbers(self):
        """Run unittest for a list with positive and negative numbers"""
        self.assertEqual(max_integer([-5, -3, 5.2]), 5.2)

    def test_non_numbers(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'm', 15])

    def test_non_list(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_char(self):
        """Run unittest for a list with characters only"""
        self.assertEqual(max_integer(['a', 'c', 'q']), 'q')

    def test_empty(self):
        """Run uittest for an empty list"""
        self.assertEqual(max_integer(), None)

    def test_string(self):
        """Run unittest for a list with strings only"""
        self.assertEqual(max_integer(["abc", "mno"]), "mno")

    def test_tuple(self):
        """Run unittest for a tuple with integers"""
        self.assertEqual(max_integer((3, 5, 78, 65, 10)), 78)
