"""
Tests the UserLocation class constructor. 
This makes sure that the program correctly identifies and can pull information from a given 
dataset. We give it a predetemined city and verify it can pulll the lat, long, and name.
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..', 'src'))
from user_location import UserLocation

class TestUserLocationConstructor(unittest.TestCase):
    def test_constructor(self):
        loc = UserLocation(42.0, -71.0, "Test City")
        print(f"Constructed: name={loc.name}, latitude={loc.latitude}, longitude={loc.longitude}")
        self.assertEqual(loc.latitude, 42.0)
        self.assertEqual(loc.longitude, -71.0)
        self.assertEqual(loc.name, "Test City")

if __name__ == "__main__":
    unittest.main()
