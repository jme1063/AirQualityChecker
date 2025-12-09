"""
    Organizes API data for easy extraction of plant species and air quality.
    - Returns a list of all plant species (plantType)
    - Returns a string of the latest air quality (airQuality)
    - Organizes a CSV file so only the latest entry is kept. This is so we can reference
      older information still while organizing current information from the API requests.
"""

import csv
import os


class DataOrganizer:
    def __init__(self):
        """
        Initializes the data_organizer object by setting up file paths for input and output CSV files.
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(script_dir)
        self.input_file = os.path.join(project_dir, 'data', 'apiRequestData.csv')
        self.output_file = os.path.join(project_dir, 'data', 'OrganizedData.csv')

    def get_all_pollen_types(self):
        """
        Reads the input CSV and returns a sorted list of all unique pollen types found.
        """
        all_pollens = set()
        with open(self.input_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                pollen_types = row[7].strip('"')
                for pollen in pollen_types.split(','):
                    all_pollens.add(pollen.strip())
        return sorted(list(all_pollens))

    def get_all_plant_species(self):
        """
        Reads the input CSV and returns a sorted list of all unique plant species found.
        """
        all_plants = set()
        with open(self.input_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                plants = row[8].strip('"')
                for plant in plants.split(','):
                    all_plants.add(plant.strip())
        return sorted(list(all_plants))

    def get_air_quality(self):
        """
        Reads the input CSV and returns the latest air quality string found.
        """
        air_quality = None
        with open(self.input_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 5:
                    air_quality = row[5].strip('"')
        return air_quality

    def sort_csv_file(self):
        """
        Reads the input CSV, keeping only the latest (last) entry, and writes organized data to the output CSV.
        The output includes city info, air quality, pollen types, and plant species, each under their own heading
        to make it easier to reference later.
        """
        last_row = None
        with open(self.input_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                last_row = row

        if last_row:
            city = last_row[0].strip('"')
            row = {
                'City': city,
                'Date': last_row[3],
                'Latitude': last_row[1],
                'Longitude': last_row[2],
                'AQI': last_row[4],
                'Air_Quality': last_row[5],
                'Main_Pollutant': last_row[6],
                'Pollen_Types': last_row[7].strip('"'),
                'Plant_Species': last_row[8].strip('"')
            }
            with open(self.output_file, 'w') as file:
                file.write(f"{row['City']},{row['Date']},{row['Latitude']},{row['Longitude']},{row['AQI']}\n")
                file.write(f"{row['Air_Quality']},{row['Main_Pollutant']}\n")
                file.write("Pollen Types:\n")
                for pollen in row['Pollen_Types'].split(','):
                    file.write(f"{pollen.strip()}\n")
                file.write("Plant Species:\n")
                for plant in row['Plant_Species'].split(','):
                    file.write(f"{plant.strip()}\n")
                file.write("\n")

    def return_all_info(self):
        """
        Organizes the data, then returns the list of plant species, the latest air quality info, and the list of pollen types.
        Returns: tuple (plant_type: list of strings, air_quality: string or None, pollen_type: list of strings)
        """
        self.sort_csv_file()
        plant_type = self.get_all_plant_species()
        air_quality = self.get_air_quality()
        pollen_type = self.get_all_pollen_types()
        return plant_type, air_quality, pollen_type