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

    def organize_data(self):
        """Test organizing data for a user"""
        allergies = AllergyInfo()
        api = GoogleMaps("EMPTY")
        main_app = App(api,allergies,"Matti")
        try:
            main_app.organize_data()
        except Exception as e:
            self.fail(f"organize_data raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()