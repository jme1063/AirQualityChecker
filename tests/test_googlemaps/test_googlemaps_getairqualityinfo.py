import unittest
import sys
import os
sys.path.append('src')
from user_location import UserLocation
from google_maps import GoogleMaps
class test(unittest.TestCase):
    def test_get_air_quality_info(self):
        """Test GoogleMaps get_air_quality_info method"""
        api = GoogleMaps("EMPTY")
        csv_path = os.path.join("data", "nh_locations.csv")
        location = UserLocation.load_from_csv()
        location = location.get("Manchester")
        try:
            air_quality = api.get_air_quality_info("Manchester", location)
            self.assertIsInstance(air_quality, dict)
        except Exception as e:
            self.fail(f"get_air_quality_info raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()