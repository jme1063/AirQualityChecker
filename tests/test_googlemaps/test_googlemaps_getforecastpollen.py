import unittest
import sys
import os
sys.path.append('src')
from user_location import UserLocation
from google_maps import GoogleMaps
class test(unittest.TestCase):
    """Test GoogleMaps get_forecast_pollen method"""
    def test_get_forecast_pollen(self):
        api_key = "EMPTY"
        gmaps = GoogleMaps(api_key)
        csv_path = os.path.join('data', 'nh_locations.csv')
        location_list = UserLocation.load_from_csv(csv_path)
        user_loc = location_list[0]  # Use the first location for testing
        result = gmaps.get_forecast_pollen(user_loc)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        print(result)
    
    def test_exception_for_bad_api_key(self):
        """Test exception handling for bad API key"""
        bad_api_key = "BAD_API_KEY"
        gmaps = GoogleMaps(bad_api_key)
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'nh_locations.csv')
        location_list = os.path.join('data', 'nh_locations.csv')
        user_loc = location_list[0]  # Use the first location for testing
        try:
            result = gmaps.get_forecast_pollen(user_loc)
            self.fail("Expected an exception due to bad API key")
        except Exception as e:
            self.assertTrue(isinstance(e, Exception))

if __name__ == '__main__':
    unittest.main()