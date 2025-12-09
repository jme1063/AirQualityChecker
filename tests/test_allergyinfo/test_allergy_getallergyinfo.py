import os
import sys
import csv
import random
import unittest
sys.path.append('src')
from allergy_info import AllergyInfo
class test(unittest.TestCase):

    def test_get_allergy_info(self):
        """Test adding a new user with allergies"""
        name = "AllergyUserNoAllergies" + str(random.randint(1, 1000))
        info = AllergyInfo()
        info.add_new_user_with_allergy(name, '["Grass", "Elm"]')
        allergies = info.get_allergy_info(name)
        self.assertTrue(allergies == ["Grass", "Elm"])

if __name__ == '__main__':
    unittest.main()