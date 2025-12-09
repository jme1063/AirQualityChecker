
"""
Unit tests for the DataOrganizer class and related functions.
These tests cover data organization, transformation, and output processes,
validating that the module correctly organizes, processes, and saves data
according to the application's requirements.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'src')))

from data_organizer import DataOrganizer


def test_plant_type_air_quality_pollen_type():
    organizer = DataOrganizer()
    plant_type, air_quality, pollen_type = organizer.return_all_info()
    print("Air Quality:", air_quality)
    print("Pollen Types:", pollen_type)
    print("Plant Types:", plant_type)

if __name__ == "__main__":
    test_plant_type_air_quality_pollen_type()
