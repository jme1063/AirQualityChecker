import unittest
import sys
import os
sys.path.append('src')
from user_location import UserLocation
from google_maps import GoogleMaps
class test(unittest.TestCase):
    def test_save_to_csv(self):
        """Test saving location data to CSV"""
        api_key = "EMPTY"
        gmaps = GoogleMaps(api_key)
        location = UserLocation(43.2081, -71.5375, "Concord")
        try:
            gmaps.save_to_csv(location)
        except Exception as e:
            self.fail(f"save_to_csv raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()