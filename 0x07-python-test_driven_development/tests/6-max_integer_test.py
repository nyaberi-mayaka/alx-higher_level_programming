#!/usr/bin/python3
"""Unitest for max_integer used to find the maximum
intger in a list of integers
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer
    tests for all exceptions in the module
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_list_positive(self):
        """Tests a list of positive integers only"""
        self.assertEqual(max_integer([2, 4, 8, 6]), 8)

    def test_list_negative(self):
        """Tests a list of negative integers only"""
        self.assertEqual(max_integer([-5, -10, -30, -2]), -2)

    def test_neg_pos(self):
        """Run unittest for a list with positive nad negative ints"""
        self.assertEqual(max_integer([10, -15, 5, 2]), 10)

    def test_beginning(self):
        """Run unittest for a max int at the start"""
        self.assertEqual(max_integer([32, 10, -45, -20, 30]), 32)

    def test_middle(self):
        """Run unittest for a max int at the middle"""
        self.assertEqual(max_integer([32, 10, 45, 20, 30]), 45)

    def test_end(self):
        """Run unittest for a max int at the end"""
        self.assertEqual(max_integer([1, 4, 12, 19]), 19)

    def test_tuple(self):
        """Run unittest for a tuple with integers"""
        self.assertEqual(max_integer((3, 5, 78, 65, 10)), 78)

    def test_char(self):
        """Run unittest for a list with characters only"""
        self.assertEqual(max_integer(['a', 'c', 'q']), 'q')

    def test_string(self):
        """Run unittest for a list with strings only"""
        self.assertEqual(max_integer(["abc", "Mno"]), "abc")

    def test_empty(self):
        """Run uittest for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Run unittest for a list with one element only"""
        self.assertEqual(max_integer([20]), 20)

    def test_empty(self):
        """Run uittest for an empty list"""
        self.assertEqual(max_integer(), None)
