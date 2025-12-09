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

    def test_set_user_location(self):
        """Test setting user location"""
        allergies = AllergyInfo()
        api = GoogleMaps("EMPTY")
        main_app = App(api,allergies,"Matti")
        main_app.set_user_location("Manchester")
        self.assertTrue(main_app.user_location.name == "Manchester")

if __name__ == '__main__':
    unittest.main()