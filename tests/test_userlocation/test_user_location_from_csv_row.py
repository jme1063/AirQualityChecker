"""
Tests the from_csv_row classmethod of UserLocation.
Makes sure the method can accurately pull information fron dictionary
"""
import unittest
import sys
import os
# Add the src directory to the path so we can import userLocation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..', 'src'))
from user_location import UserLocation

class TestUserLocationFromCSVRow(unittest.TestCase):
    def test_from_csv_row(self):
        """
        Test that from_csv_row creates a UserLocation from a dictionary.
        """
        row = {'latitude': '42.0', 'longitude': '-71.0', 'name': 'Test City'}
        loc = UserLocation.from_csv_row(row)
        print(f"Loaded from CSV row: name={loc.name}, latitude={loc.latitude}, longitude={loc.longitude}")
        self.assertEqual(loc.latitude, 42.0)
        self.assertEqual(loc.longitude, -71.0)
        self.assertEqual(loc.name, "Test City")

if __name__ == "__main__":
    unittest.main()
