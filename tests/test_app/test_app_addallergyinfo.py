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

    def test_add_allergy_info(self):
        """Test adding allergy info to a user"""
        allergies = AllergyInfo()
        api = GoogleMaps("EMPTY")
        rand_name = "TestUser" + random.randint(1,1000).__str__()
        main_app = App(api,allergies, rand_name)
        main_app.add_allergy_info("cat dander")
        allergyList = main_app.get_allergy_info()
        self.assertTrue(allergyList == ["cat dander"])

if __name__ == '__main__':
    unittest.main()