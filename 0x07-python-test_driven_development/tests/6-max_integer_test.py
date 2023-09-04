"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests for max_integer."""

    def test_zero_number(self):
        """Test with 0 """
        self.assertEqual(max_integer([0, 0]), 0)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_ordered_list(self):
        """Test an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list."""
        self.assertEqual(max_integer([3, 2, 4, 1]), 4)

    def test_repeated_number(self):
        """Test repeated numbers"""
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_max_at_begginning(self):
        """Test a list with different position of max value."""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_neg_numbers(self):
        """Test for negative numbers"""
        self.assertEqual(max_integer([-76, -22, -16, -10]), -10)

    def test_tuple_in_a_list(self):
        """Test tuple inside the passed list """
        with self.assertRaises(TypeError):
            max_integer([1, (7, 2, 96)])

    def test_one_element_list(self):
        """Test for one value."""
        self.assertEqual(max_integer([100]), 100)

    def test_float(self):
        """Test for floats."""
        f = [1.8, 9.3, -4.8, 2.2, -0.2]
        self.assertEqual(max_integer(f), 9.3)

    def test_list_with_loop(self):
        """Test with a loop"""
        my_list = [2, 4, 3, 8, 10]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 50)

    def test_int_and_float(self):
        """Test list with int and float."""
        values = [8.5, 2.1, 8.1, -52, 8]
        self.assertEqual(max_integer(values), 8.5)

    def test_string_number_in_list(self):
        """Test for string in list"""
        with self.assertRaises(TypeError):
            max_integer([0, 'k'])


if __name__ == '__main__':
    unittest.main()