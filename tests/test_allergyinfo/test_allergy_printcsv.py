import os
import sys
import csv
import random
import unittest
sys.path.append('src')
from allergy_info import AllergyInfo
class test(unittest.TestCase):

    def test_print_csv(self):
        """Test printing allergy info from CSV"""
        with open('data/allergies.csv', mode='r') as file:
            csv_file = csv.DictReader(file)
            for lines in csv_file:
                print(lines)

if __name__ == '__main__':
    unittest.main()