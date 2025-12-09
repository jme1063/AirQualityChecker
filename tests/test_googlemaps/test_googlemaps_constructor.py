import unittest
import sys
import os
sys.path.append('src')
from user_location import UserLocation
from google_maps import GoogleMaps
class test(unittest.TestCase):
    """Test GoogleMaps constructor"""
    def test_constructor(self):
        api_key = "EMPTY"
        gmaps = GoogleMaps(api_key)
        self.assertEqual(gmaps.api_key, api_key)

if __name__ == '__main__':
    unittest.main()