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

    def test_allergy_constructor(self):
        """Test AllergyInfo constructor"""
        allergies = AllergyInfo()
        self.assertIsInstance(allergies, AllergyInfo)

if __name__ == '__main__':
    unittest.main()