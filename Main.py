"""
main.py - Main program file for the NH Air Quality & Pollen App

Currently, It imports the userLocation module to use the userLocation class objects.
"""

import sys
import os


# Add the src directory to the path so we can import userLocation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from user_location import UserLocation
from google_maps import GoogleMaps
from runner import Runner

def main():
    main_run = Runner()
    main_run.run()

    """
    # Quick test - get Manchester data and save to CSV
    # Verified working. commenting out so we dont call the api key every 
    # time we test main
    gmaps = GoogleMaps("EMPTY")
    gmaps.saveToCSV(first_location)  
    print("Saved information to CSV file!")
    """



if __name__ == "__main__":

    main()
