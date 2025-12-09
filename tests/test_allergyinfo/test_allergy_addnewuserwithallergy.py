import os
import sys
import csv
import random
import unittest
sys.path.append('src')
from allergy_info import AllergyInfo
class test(unittest.TestCase):
    def test_add_new_user(self):
        name = "NewUser" + str(random.randint(1, 1000))
        allergy_list = '["pollen", "dust"]'
        info = AllergyInfo()
        info.add_new_user_with_allergy(name, allergy_list)

    def test_add_existing_user(self):
        name = "Matti"
        allergy_list = '["pollen", "dust", "existinguser"]'
        info = AllergyInfo()
        response = info.add_new_user_with_allergy(name, allergy_list)
        self.assertTrue(response is None)

if __name__ == '__main__':
    unittest.main()