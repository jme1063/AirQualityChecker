
"""
Tests extraction of plant species, air quality, and pollen types from the organized data.
Mainly also tests code on newest data set. this is commented out by default as it makes API calls
so uncomment if you wish to test this specifically.
"""

import sys
import os

 # Ensure src directory is in the path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..', 'src'))

from google_maps import GoogleMaps
from user_location import UserLocation
from data_organizer import DataOrganizer

"""
 #Used to test dataOrganization on newest data. 
 # commented out as It will make API calsl. Please use sparingly
api_key = "EMPTY"
manchester = UserLocation(42.9956, -71.4548, "Manchester")
gmaps = GoogleMaps(api_key)
print("Testing save_to_csv...")
gmaps.save_to_csv(manchester)  # Calls API and saves result
print("Done!")
"""

def test_data_organizer():
    """
    Unit test for data_organizer function to make sure data is properly returned
    """
    print("\n=== TESTING DATA ORGANIZER ===")
    organizer = DataOrganizer()

    # Retrieve all three data types from the organized CSV
    plant_species, air_quality, pollen_type = organizer.return_all_info()

    print(f"\nPlant species list contains {len(plant_species)} species:")

    print(f"\nLatest air quality: {air_quality}")

    print(f"\nPollen types list contains {len(pollen_type)} types:")

    print("\nData organizer test completed successfully!")

if __name__ == "__main__":
    test_data_organizer()