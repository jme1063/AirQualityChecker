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
    def test_get_allergyInfo(self):
        allergies = AllergyInfo()
        api = GoogleMaps("EMPTY")
        main_app = App(api,allergies,"Matti")
        allergy_list = main_app.get_allergy_info()
        self.assertTrue(allergy_list == ["pollen", "dust"])

if __name__ == '__main__':
    unittest.main()