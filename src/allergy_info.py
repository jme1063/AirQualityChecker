import csv


class AllergyInfo:
    """Class to manage allergy information for users"""
    def __init__(self):
        """Constructor for AllergyInfo class"""
        pass

    def update_allergy(self, name, allergy):
        """Updates the allergy information for a user by adding a new allergy.
        Arguments: String name -- name of the user
                   String -- allergy to be added"""
        update_list = []
        with open('data/allergies.csv', mode='r') as file:
            csv_file = csv.DictReader(file)
            for rows in csv_file:
                update_list.append(rows)
        found = False
        for rows in update_list:
            if rows["Name"] == name:
                found = True
                to_list = eval(rows["AllergyList"])
                to_list.append(allergy)
                rows["AllergyList"] = to_list
        with open('data/allergies.csv', mode='w', newline='') as file:
            fieldnames = ['Name', 'AllergyList']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(update_list)

    def add_new_user_with_allergy(self, name, allergy_list):
        """Adds a new user with an initial allergy list
        Arguments: String name -- name of the user
                   String allergy_list -- list of allergies in string format"""
        
        with open('data/allergies.csv', mode='r') as file:
            csv_file = csv.DictReader(file)
            for rows in csv_file:
                if rows["Name"] == name:
                    return None
        with open('data/allergies.csv', mode='a', newline='') as file:
            fieldnames = ['Name', 'AllergyList']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'Name': name, 'AllergyList': allergy_list})

    def add_new_user(self, name):
        """Adds a new user without any allergies
        Arguments: String name -- name of the user"""
        with open('data/allergies.csv', mode='r') as file:
            csv_file = csv.DictReader(file)
            for rows in csv_file:
                if rows["Name"] == name:
                    return None
        with open('data/allergies.csv', mode='a', newline='') as file:
            fieldnames = ['Name', 'AllergyList']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'Name': name, 'AllergyList': '[]'})

    def get_allergy_info(self, name):
        """Retrieves the allergy information for a user
        Arguments: String name -- name of the user"""
        with open('data/allergies.csv', mode='r') as file:
            csv_file = csv.DictReader(file)
            for rows in csv_file:
                if rows["Name"] == name:
                    return eval(rows["AllergyList"])
        return None

                    
            
            