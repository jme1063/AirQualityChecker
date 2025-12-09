# Allergen Checker

## Overview

[Allergen Checker] is an application designed to help users track and manage their allergies based on real-time air quality and pollen data. The user can create an allergen profile that includes all of their allergies and location so they can get quick up-to-date information on the air quality in their area, or they can simply input a location to grab generic information about the air quality in a given area.

## Features

- User registration with allergy and location input
- Integration with Google Maps for air quality and pollen data
- Ability to add and update user allergies

## Domain Model

The core classes in the project include:

- **User**: Stores user allergies and location, and can view reports.
- **userLocation**: Represents a user's geographic location.
- **googleMaps**: Handles fetching air quality and pollen data from external APIs.
- **allergyInfo**: Manages allergy data and user-specific allergy lists.
- **OrganizeData**: a class that organizes the information gained from the API request.

## File Structure

```
project-jackie-matti/
├── data/           # Data files and resources
├── design/         # Design documents (e.g., class diagrams)
├── process/        # Project process documentation
├── src/            # Source code
├── tests/          # Unit and integration tests
├── main.py         # Main application entry point
├── pyproject.toml  # requirements.txt but for use with poetry
├── poetry.lock     # poetry log when installing files
└── README.md       # Project documentation

```

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/fall-2025-comp-730/project-jackie-matti.git
   cd project-jackie-matti
   ```

2. **Run the application:**
   ```sh
   python main.py
   ```

## Running the program using Poetry

1. **Make sure poetry is installed on your device**
   - you will need to install poetry onto your device. I managed to do this on windows 10 with:
   ```

   ```
   

2. **Install dependencies as needed**
   ```
   poetry install
   ```
   - this will make sure you have the correct version of any dependencies needed on your device, and will install or update as needed

3. **Start poetry session**
   ```
   poetry shell
   ```
   - This opens up a poetry enviornment to run the project inside

4. **Running the program**
   ```
   python [script-to-run.py] i.e: python Main.py
   ```
   - this will run a given script inside the poetry shell

## License

This project is for educational purposes and may be subject to your institution's policies.

---