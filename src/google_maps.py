##AirQuality = EMPTY
import requests
import csv


class GoogleMaps:
    """
    Class used to send requests to the Google Maps API
    """
    def __init__(self, api_key):
        """
        Initialize object attributes
        """
        self.api_key = api_key

    def get_current_conditions_quality(self, user_location):
        """
        Get current air quality conditions for a given user location
        Arguments: UserLocation user_location -- user location object
        Returns: JSON data from the API request
        """
        url = "https://airquality.googleapis.com/v1/currentConditions:lookup?key=" + self.api_key
        body = {
            "location": {
                "latitude": user_location.latitude,
                "longitude": user_location.longitude
            }
        }
        data = requests.post(url, json=body)
        return data.json()

    def get_forecast_pollen(self, user_location):
        """Get forecasted pollen levels for a given user location
        Arguments: UserLocation user_location -- user location object
        Returns: JSON data from the API request"""
        url = (
            "https://pollen.googleapis.com/v1/forecast:lookup?key=" + self.api_key +
            "&location.longitude=" + str(user_location.longitude) +
            "&location.latitude=" + str(user_location.latitude) +
            "&days=1"
        )
        data = requests.get(url)
        return data.json()

    def get_air_quality_info(self, location_name, user_location):
        """
          Get the air quality data from the API request and saves into a dict
            Arguments: String location_name -- name of the location
                        UserLocation user_location -- user location object
                        Returns: Dict with cleaned air quality data
        """
        raw_data = self.get_current_conditions_quality(user_location)
        aqi_number = raw_data['indexes'][0]['aqi']
        air_category = raw_data['indexes'][0]['category']
        main_pollutant = raw_data['indexes'][0]['dominantPollutant']

        clean_data = {
            'location': location_name,
            'lat': user_location.latitude,
            'lon': user_location.longitude,
            'aqi': aqi_number,
            'category': air_category,
            'pollutant': main_pollutant
        }
        return clean_data

    def get_pollen_info(self, location_name, user_location):
        """
           Gets the pollen data from the API request and stores in a dict
           Arguments: String location_name -- name of the location
                      UserLocation user_location -- user location object
           Returns: Dict with cleaned pollen data
        """
        raw_data = self.get_forecast_pollen(user_location)
        date_info = raw_data['dailyInfo'][0]['date']
        readable_date = f"{date_info['month']}/{date_info['day']}/{date_info['year']}"

        pollen_type_list = []
        for item in raw_data['dailyInfo'][0]['pollenTypeInfo']:
            pollen_type_list.append(item['displayName'])

        plant_list = []
        for item in raw_data['dailyInfo'][0]['plantInfo']:
            plant_list.append(item['displayName'])

        clean_data = {
            'location': location_name,
            'date': readable_date,
            'pollen': ",".join(pollen_type_list),
            'plants': ",".join(plant_list)
        }
        return clean_data

    def save_to_csv(self, user_location):
        """
           Get data extracted from pollen and air quality functions
           and save to CSV
           Arguments: UserLocation user_location -- user location object
        """
        air_data = self.get_air_quality_info(user_location.name, user_location)
        pollen_data = self.get_pollen_info(user_location.name, user_location)

        csv_file_path = 'data/apiRequestData.csv'
        with open(csv_file_path, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            data_row = [user_location.name, user_location.latitude, user_location.longitude, pollen_data['date'],
                       air_data['aqi'], air_data['category'], air_data['pollutant'],
                       pollen_data['pollen'], pollen_data['plants']]
            writer.writerow(data_row)

        print(f"Successfully extracted air and pollen data for {user_location.name}!")
        return air_data, pollen_data