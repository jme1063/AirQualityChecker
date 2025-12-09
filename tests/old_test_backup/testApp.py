import sys
import os
import random

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append('src')
from user_location import UserLocation
from google_maps import GoogleMaps
from allergy_info import AllergyInfo
from app import App

import unittest
class test_app(unittest.TestCase):
    def test_get_allergyInfo(self):
        allergies = AllergyInfo()
        api = GoogleMaps("EMPTY")
        main_app = App(api,allergies,"Matti")
        allergy_list = main_app.get_allergy_info()
        self.assertTrue(allergy_list == ["pollen", "dust"])

    def test_add_allergy_info(self):
        allergies = AllergyInfo()
        api = GoogleMaps("EMPTY")
        rand_name = "TestUser" + random.randint(1,1000).__str__()
        main_app = App(api,allergies, rand_name)
        main_app.add_allergy_info("cat dander")
        allergyList = main_app.get_allergy_info()
        self.assertTrue(allergyList == ["cat dander"])

    def test_set_user_location(self):
        allergies = AllergyInfo()
        api = GoogleMaps("EMPTY")
        main_app = App(api,allergies,"Matti")
        main_app.set_user_location("Manchester")
        self.assertTrue(main_app.user_location.name == "Manchester")

    def test_fetch_air_data(self):
        allergies = AllergyInfo()
        api = GoogleMaps("EMPTY")
        main_app = App(api,allergies,"Matti")
        main_app.set_user_location("Manchester, NH")
        try:
            main_app.fetch_air_data(api)
        except Exception as e:
            self.fail(f"fetch_air_data raised an exception: {e}")

    def organize_data(self):
        allergies = AllergyInfo()
        api = GoogleMaps("EMPTY")
        main_app = App(api,allergies,"Matti")
        try:
            main_app.organize_data()
        except Exception as e:
            self.fail(f"organize_data raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()
