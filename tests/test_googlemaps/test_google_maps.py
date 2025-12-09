import unittest
import sys
import os

# Add the src directory to the path so we can import userLocation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from user_location import UserLocation
from google_maps import GoogleMaps

class TestGoogleMaps(unittest.TestCase):
    def test_constructor(self):
        api_key = "EMPTY"
        gmaps = GoogleMaps(api_key)
        self.assertEqual(gmaps.api_key, api_key)

    def test_get_current_conditions_quality(self):
        api_key = "EMPTY"
        gmaps = GoogleMaps(api_key)
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'nh_locations.csv')
        location_list = UserLocation.load_from_csv(csv_path)
        user_loc = location_list[0]  # Use the first location for testing
        result = gmaps.get_current_conditions_quality(user_loc)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        print(result)

    def test_get_forecast_pollen(self):
        api_key = "EMPTY"
        gmaps = GoogleMaps(api_key)
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'nh_locations.csv')
        location_list = UserLocation.load_from_csv(csv_path)
        user_loc = location_list[0]  # Use the first location for testing
        result = gmaps.get_forecast_pollen(user_loc)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        print(result)

    def test_exception_for_bad_api_key(self):
        bad_api_key = "BAD_API_KEY"
        gmaps = GoogleMaps(bad_api_key)
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'nh_locations.csv')
        location_list = UserLocation.load_from_csv(csv_path)
        user_loc = location_list[0]  # Use the first location for testing
        try:
            result = gmaps.get_forecast_pollen(user_loc)
            self.fail("Expected an exception due to bad API key")
        except Exception as e:
            self.assertTrue(isinstance(e, Exception))

    def test_save_to_csv(self):
        api_key = "EMPTY"
        gmaps = GoogleMaps(api_key)
        location = UserLocation(43.2081, -71.5375, "Concord")
        try:
            gmaps.save_to_csv(location)
        except Exception as e:
            self.fail(f"save_to_csv raised an exception: {e}")
if __name__ == '__main__':
    unittest.main()