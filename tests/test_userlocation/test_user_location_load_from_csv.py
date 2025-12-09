
"""
Tests the load_from_csv classmethod of UserLocation.
Makes sure the method can accurately pull information from the nh_location csv file for use
"""
import unittest
import os
import sys
# Add the src directory to the path so we can import userLocation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..', 'src'))
from user_location import UserLocation

class TestUserLocationLoadFromCSV(unittest.TestCase):
    def test_load_from_csv(self):
        """
        Test that load_from_csv loads UserLocation objects from nh_locations.csv.
        """
        csv_path = os.path.join(os.path.dirname(__file__), '../..', 'data', 'nh_locations.csv')
        locations = UserLocation.load_from_csv(csv_path)
        self.assertGreater(len(locations), 0)

        # Check the first location matches Manchester
        first = locations[0]

        # I also have us print information so we can verify what is being pulled out
        print(f"Loaded Manchester: name={first.name}, latitude={first.latitude}, longitude={first.longitude}")
        self.assertEqual(first.name, "Manchester")
        self.assertAlmostEqual(first.latitude, 42.9956, places=4)
        self.assertAlmostEqual(first.longitude, -71.4548, places=4)

if __name__ == "__main__":
    unittest.main()
