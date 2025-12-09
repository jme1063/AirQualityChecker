import sys
import os
import random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append('src')
from app import App
from user_location import UserLocation
from google_maps import GoogleMaps
from allergy_info import AllergyInfo
import unittest
class TestApp(unittest.TestCase):
    def test_get_allergy_info(self):
        allergies = AllergyInfo()
        rand_name = "TestUser" + str(random.randint(1, 1000))
        api = GoogleMaps("EMPTY")
        main_app = App(api, allergies, rand_name)
        allergies.add_new_user_with_allergy(rand_name, ["pollen", "dust"])
        allergy_list = main_app.get_allergy_info()
        self.assertTrue(allergy_list == ["pollen", "dust"])

    def test_add_allergy_info(self):
        allergies = AllergyInfo()
        api = GoogleMaps("EMPTY")
        rand_name = "TestUser" + str(random.randint(1, 1000000))
        main_app = App(api, allergies, rand_name)
        main_app.add_allergy_info("testAllergy")
        allergy_list = main_app.get_allergy_info()
        self.assertTrue(allergy_list == ["testAllergy"])
    

if __name__ == '__main__':
    unittest.main()
