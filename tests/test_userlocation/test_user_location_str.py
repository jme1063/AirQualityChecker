"""
File: test_user_location_str.py
Tests the __str__ method of UserLocation.
"""
import unittest
import sys
import os
# Add the src directory to the path so we can import userLocation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..', 'src'))
from user_location import UserLocation

class TestUserLocationStr(unittest.TestCase):
    def test_str(self):
        """
        Test that __str__ returns the correct string representation.
        """
        loc = UserLocation(42.0, -71.0, "Test City")
        self.assertEqual(str(loc), "Test City (42.0, -71.0)")

if __name__ == "__main__":
    unittest.main()
