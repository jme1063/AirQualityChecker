import os
import sys
import csv
import random
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append('src')
from allergy_info import AllergyInfo


class TestAllergyInfo(unittest.TestCase):
    def test_print_csv(self):
        with open('data/allergies.csv', mode='r') as file:
            csv_file = csv.DictReader(file)
            for lines in csv_file:
                print(lines)

    def test_update_allergy(self):
        info = AllergyInfo()
        info.update_allergy("Test", "rabbit")

    def test_update_allergy_non_existing_user(self):
        allergy = "alder"
        name = "NonExistingUser"
        info = AllergyInfo()
        info.update_allergy(name, allergy)
        response = info.get_allergy_info(name)
        self.assertTrue(response is None)

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

    def test_get_allergy_info(self):
        name = "AllergyUserNoAllergies" + str(random.randint(1, 1000))
        info = AllergyInfo()
        info.add_new_user_with_allergy(name, '["Grass", "Elm"]')
        allergies = info.get_allergy_info(name)
        self.assertTrue(allergies == ["Grass", "Elm"])

    def test_new_allergy_user_with_no_allergies(self):
        name = "AllergyUserNoAllergies" + str(random.randint(1, 1000))
        info = AllergyInfo()
        info.add_new_user(name)
        allergies = info.get_allergy_info(name)
        self.assertTrue(allergies == [])

if __name__ == '__main__':
    unittest.main()