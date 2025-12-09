import os
import sys
import csv
import random
import unittest
sys.path.append('src')
from allergy_info import AllergyInfo
class test(unittest.TestCase):
    def test_new_allergy_user_with_no_allergies(self):
        name = "AllergyUserNoAllergies" + str(random.randint(1, 1000))
        info = AllergyInfo()
        info.add_new_user(name)
        allergies = info.get_allergy_info(name)
        self.assertTrue(allergies == [])

if __name__ == '__main__':
    unittest.main()