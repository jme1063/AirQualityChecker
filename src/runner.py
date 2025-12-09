from google_maps import GoogleMaps
from app import App
from allergy_info import AllergyInfo

class Runner():
    """main logic class for the application"""
    google_maps_api = GoogleMaps('EMPTY')
    allergy_info = AllergyInfo()
    def __init__(self):
        """Constructor for Runner class"""
        print("Welcome to our air quality report app")
        self.input_name = input("Please enter your name: ")

    def run(self):
        """Runs the main application loop"""
        app = App(Runner.google_maps_api, Runner.allergy_info, self.input_name)
        while True:
            choice = input("Do you want to add an allergy? (yes/no)")
            if app.get_allergy_info() is None:
                if choice.lower() == 'no':
                    print("You must add at least one allergy to proceed.")
                    choice = 'yes'
            if choice.lower() == 'yes':
                allergy = input("Please enter your allergy: ")
                app.add_allergy_info(allergy)
            elif choice.lower() == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
            choice2 = input("Do you want to add another allergy? (yes/no)")
            if choice2.lower() == 'no':
                break

        while True:
            input_location = input("Please enter your location (e.g., Concord, NH): ")
            app.set_user_location(input_location)
            if app.user_location is not None:
                break
            else:
                print("Location not found. Please try again.")    
        app.fetch_air_data()
        app.generate_report()
        print("Would you like to go again? (yes/no)")
        again = input()
        if again.lower() == 'yes':
            self.run()
        else:
            print("Thank you for using the air quality report app. Goodbye!")
            return None
