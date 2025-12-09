"""
userLocation.py - Implementation of userLocation class from domain model
"""

import csv

class UserLocation:
    """
    Represents a geographical location with coordinates and name.
    """

    def __init__(self, latitude: float, longitude: float, name: str):
        """
        initialize object attributes
        """
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

    def __str__(self):
        """
        Currently combines object attributes and returns it in string format.
        """
        name_part = self.name
        coordinates_part = f"({self.latitude}, {self.longitude})"
        full_string = f"{name_part} {coordinates_part}"
        return full_string

    @classmethod
    def from_csv_row(cls, row_data: dict):
        """
        Pulls information from the manually created location dataset and creates userLocation based
        off of the name the user gave
        Expects a dictionary with keys: name, latitude, longitude
        """
        return cls(
            latitude=float(row_data['latitude']),
            longitude=float(row_data['longitude']),
            name=row_data['name']
        )

    @classmethod
    def load_from_csv(cls, csv_file_path: str):
        """
        Load all user_location objects from a CSV file.
        Returns a list of user_location objects.
        """
        locations = []

        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                location = cls.from_csv_row(row)
                locations.append(location)

        return locations
