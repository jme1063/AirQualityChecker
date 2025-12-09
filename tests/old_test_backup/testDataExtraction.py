"""
Quick test of the GoogleMaps saveToCSV function
this will call the api in order to find information.
"""


import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..', 'src'))

from data_organizer import DataOrganizer
from google_maps import GoogleMaps
from user_location import UserLocation


# Test the saveToCSV function. This will call the API key and use tokens.
API_KEY = "EMPTY"
gmaps = GoogleMaps(API_KEY)

# Create a userLocation object for Manchester, NH
manchester = UserLocation(42.9956, -71.4548, "Manchester, NH")  # Fixed parameter order

print("Testing saveToCSV...")
gmaps.save_to_csv(manchester)  # Now passing userLocation object
print("Done!")

def test_data_organizer():
    """
    Unit test for DataOrganizer functions
    """
    print("\n=== TESTING DATA ORGANIZER ===")
    organizer = DataOrganizer()
    # Test organizing data
    print("Testing sort_csv_file()...")
    organizer.sort_csv_file()
    # Test getting all plant species
    print("\nTesting get_all_plant_species()...")
    plant_species = organizer.get_all_plant_species()
    
    print(f"\nPlant species list contains {len(plant_species)} species:")
    for i, plant in enumerate(plant_species, 1):
        print(f"  {i}. {plant}")
    
    print("\nData organizer test completed successfully!")
    return plant_species

if __name__ == "__main__":
    # Run the data organizer test
    plant_list = test_data_organizer()
    print(f"\nFinal plant species list: {plant_list}")
