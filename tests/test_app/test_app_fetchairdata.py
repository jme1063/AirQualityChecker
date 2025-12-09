import sys
import os
import random
sys.path.append('src')
from user_location import UserLocation
from google_maps import GoogleMaps
from allergy_info import AllergyInfo
from app import App

import unittest

class test(unittest.TestCase):

    def test_fetch_air_data(self):
        """Test fetching air data for a user location"""
        allergies = AllergyInfo()
        api = GoogleMaps("EMPTY")
        main_app = App(api,allergies,"Matti")
        main_app.set_user_location("Manchester")
        try:
            main_app.fetch_air_data()
        except Exception as e:
            self.fail(f"fetch_air_data raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()