import sys
import os
import random
import unittest
sys.path.append('src')
from user_location import UserLocation
from google_maps import GoogleMaps
from allergy_info import AllergyInfo
from app import App

class test(unittest.TestCase):

    def test_app_constructor(self):
        """Test App constructor"""
        allergies = AllergyInfo()
        api = GoogleMaps("EMPTY")
        rand_name = "TestUser" + random.randint(1,1000).__str__()
        main_app = App(api,allergies, rand_name)
        self.assertTrue(main_app.name == rand_name)
        self.assertTrue(main_app.maps_api == api)
        self.assertTrue(main_app.allergy_info == allergies)

if __name__ == '__main__':
    unittest.main()