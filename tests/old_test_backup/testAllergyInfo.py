import os
import sys
import csv
import random
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from allergy_info import AllergyInfo


class TestAllergyInfo(unittest.TestCase):
    
    def test_print_csv(self):
        """Utility test to print the contents of the allergies.csv file"""
        with open('data/allergies.csv', mode='r') as file:
            csv_file = csv.DictReader(file)
            for lines in csv_file:
                print(lines)
                #for rows in lines:
                   # print(rows)

    def test_update_allergy(self):
        """Test updating allergy information for an existing user"""
        allergy = "alder"
        name = "Matti"
        allergy_info = AllergyInfo()
        allergy_info.update_allergy("Test", "rabbit") 

    def test_update_allergy_non_existing_user(self):
        """Test updating allergy information for a non-existing user"""
        allergy = "alder"
        name = "NonExistingUser"
        allergy_info = AllergyInfo()
        allergy_info.update_allergy(name, allergy)
        self.assertEqual(allergy_info.get_allergy_info(name), None)

    def test_add_new_user(self):
        """Test adding a new user with allergy information"""
        name = "NewUser" + random.randint(1,1000).__str__()
        allergy_list = '["pollen", "dust"]'
        allergy_info = AllergyInfo()
        allergy_info.add_new_user_with_allergy(name, allergy_list)

    def test_add_existing_user(self):
        """Test adding an existing user with allergy information"""
        name = "Matti"
        allergy_list = '["pollen", "dust", "existinguser"]'
        allergy_info = AllergyInfo()
        self.assertEqual(allergy_info.add_new_user_with_allergy(name, allergy_list), None)

    def test_get_allergy_info(self):
        """Test retrieving allergy information for an existing user"""
        name = "Matti"
        allergy_info = AllergyInfo()
        allergies = allergy_info.get_allergy_info(name)
        self.assertTrue(allergies == ["pollen", "dust"])
    
    def test_new_allergy_user_with_no_allergies(self):
        """Test adding a new user with no allergies"""
        name = "AllergyUserNoAllergies" + random.randint(1,1000).__str__()
        allergy_info = AllergyInfo()
        allergy_info.add_new_user(name)
        allergies = allergy_info.get_allergy_info(name)
        self.assertTrue(allergies == [])

if __name__ == '__main__':
    unittest.main()