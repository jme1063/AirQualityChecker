"""
This unit test is for the generateReport function of App.py

it now has the user create a new user account, or read one in
"""


import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from app import App
from google_maps import GoogleMaps
from allergy_info import AllergyInfo
from data_organizer import DataOrganizer


def main():
    print("Welcome to the Allergy Report Generator!")
    # Profile prompt
    has_profile = input("Do you have a user profile? (y/n): ").strip().lower()

    if has_profile == 'y':
        user_name = input("Enter your user name: ").strip()
        update_allergy = input("Do you need to update your allergy information? (y/n): ").strip().lower()
        if update_allergy == 'y':
            allergy = input("Enter your updated allergy (or leave blank if none): ").strip()
        else:
            allergy = ""
    else:
        make_profile = input("Would you like to make a profile? (y/n): ").strip().lower()
        if make_profile == 'y':
            user_name = input("Enter a new user name: ").strip()
        else:
            user_name = ""
        allergy = input("Enter an allergy (or leave blank if none): ").strip()

    # Location prompt (required)
    location_name = input("Enter a New Hampshire location: ").strip()

    # Setup objects
    allergies = AllergyInfo()
    api = GoogleMaps("EMPTY")
    main_app = App(api, allergies, user_name)
    main_app.set_user_location(location_name)
    if allergy:
        main_app.add_allergy_info(allergy)

    # Fetch new air and pollen data and update apiRequestData.csv
    main_app.maps_api.save_to_csv(main_app.user_location)
    # Update organized_data.csv with a new entry
    organizer = DataOrganizer()
    organizer.return_all_info()

    csv_path = os.path.join("data", "report.csv")
    print("\n--- Begin CLI Output for Allergy Report ---")
    main_app.generate_report(csv_path=csv_path)
    print("--- End CLI Output for Allergy Report ---\n")

    # Optionally, show CSV output
    if os.path.exists(csv_path):
        print("CSV report generated at:", csv_path)
        with open(csv_path, newline="") as f:
            print("\nCSV Output:")
            for line in f:
                print(line.strip())

if __name__ == '__main__':
    main()
