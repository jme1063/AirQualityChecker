
from user_location import UserLocation
from  google_maps import GoogleMaps
from data_organizer import DataOrganizer
from allergy_info import AllergyInfo
"""Implementation of app class from domain model"""

import csv
import os
from datetime import datetime


class App:
    """Main interface between main and the domain model classes"""
    def __init__(self, maps_api, allergy_info_obj, name):
        """Constructor that takes in a google_maps object, allergy_info object, and user name
        Arguements: GoogleMaps maps_api -- google maps api object
                    AllergyInfo allergy_info_obj -- allergy info object
                    String name -- name of the user"""
        self.maps_api = maps_api
        self.allergy_info = allergy_info_obj
        self.user_location = None
        self.name = name

    def set_user_location(self, location):
        """Sets the user location based on a location name
        Arguments: String location -- name of the location"""
        locations = UserLocation.load_from_csv('data/nh_locations.csv')
        for loc in locations:
            if loc.name == location:
                self.user_location = loc
                return
        raise ValueError("Location not found")

    def get_allergy_info(self):
        """Gets the allergy information for the user
        Returns: List of allergies for the user"""
        return self.allergy_info.get_allergy_info(self.name)

    def add_allergy_info(self, allergy):
        """Adds allergy information for the user with an allergy string as input
        Arguments: String allergy -- allergy to be added"""
        if self.get_allergy_info() is not None:
            self.allergy_info.update_allergy(self.name, allergy)
        else:
            self.allergy_info.add_new_user_with_allergy(self.name, str([allergy]))

    def fetch_air_data(self):
        """Fetches air quality data for the user's location using the google_maps object"""
        if self.user_location is None:
            raise ValueError("User location not set")
        self.maps_api.save_to_csv(self.user_location)

    def generate_report(self, csv_path="data/report.csv"):
        """
        Generates a report using organized data from data_organizer, prints it, and writes it to a CSV file.
        """
        # Update apiRequestData.csv with latest data before organizing
        self.fetch_air_data()
        curr_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        users_name = self.name or ""
        user_allergies = self.get_allergy_info() or []
        location = self.user_location.name

        # take the 3 returned values from the final function in data_organizer.py
        sorted_for_report = DataOrganizer()
        result = sorted_for_report.return_all_info()
        plant_species = result[0]
        air_quality = result[1]
        pollen_types = result[2]

        # Find allergy risks 
        allergy_risks = []
        for pollen in pollen_types:
            if pollen in user_allergies:
                allergy_risks.append(pollen)
        for plant in plant_species:
            if plant in user_allergies and plant not in allergy_risks:
                allergy_risks.append(plant)

        # Print report
        print("\nAllergy Report")

        if users_name:
            print("User:", users_name, curr_time)
        else:
            print("Date:", curr_time)
        print("Location:", location)
        print("Air Quality:", air_quality)

        print("Current Pollen Types in Air:", ', '.join(pollen_types) if pollen_types else 'None')
        print("Plant Species:", ', '.join(plant_species) if plant_species else 'None')

        if allergy_risks:
            print("Warning: You are allergic to", ', '.join(allergy_risks), "! Be cautious today.")
        else:
            print("No allergy risks detected for the hour.")

        # Write CSV
        with open(csv_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                users_name,
                curr_time,
                location,
                air_quality,
                ", ".join(pollen_types) if pollen_types else 'None',
                ", ".join(plant_species) if plant_species else 'None',
                ", ".join(allergy_risks) if allergy_risks else 'None'
            ])
        
