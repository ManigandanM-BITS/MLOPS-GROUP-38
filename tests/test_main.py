"""
Test module for testing the main module.
"""

import os
import unittest
from src.main import add

class TestMain(unittest.TestCase):
    """
    Unit test class for testing the add function in the main module.
    """

    def test_add(self):
        """
        Test case for the add function.
        """
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

if __name__ == "__main__":
    unittest.main()
