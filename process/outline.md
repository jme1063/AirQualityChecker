# Project Idea (Vision):
Create an app that gets air quality data and pollen information for various New Hampshire locations, and generates a text report based on the air quality information and the pollen information of the various plant species.


## Scope:
Focus on gathering data based on locations in New Hampshire, and generating a report in text/ascii form.

## Stakeholders:
Users with enviromental and health concerns

Govermental offices

UNH faculty/students

## Use Cases:

### Use Case 1:

#### Saving allergen profiles to keep track of personal allergen information which will be used in the API requests

User logs in with their name

User inputs any allergies they want to add

System saves it to a CSV file


### Use Case 2:

#### Creating a new user profile with their information saved

User inputs a name for their profile


System appends it to the CSV file


### Use Case 3:

#### Viewing personalized reports that highlight allergens matching a user’s saved profile using the saved allergen profiles and the API request wrapper

User logs in by inputting name

User selects location

User requests report

System displays report information


### Use Case 4:

#### User's reports are saved so they are not lost upon restart

User logs in by inputting name

User selects location

User asks for report

System outputs report and after saving it to a csv


## Internal Systems:

Saving a set of allergies

Set of New Hampshire locations to choose from

Generation of data report

Poetry


## External Systems:

Google pollen and air quality API: Linked below in Dataset

Visual Studio Code for development: https://code.visualstudio.com

Github

## Dataset:

Both datasets are updated hourly and requested each time a user asks for a report.

Dataset 1:

Pollen Information

Source: Google Weather API https://developers.google.com/maps/documentation/weather?utm_source=chatgpt.com

Creator: Google Maps Platform

Publisher: Google

License: Google API and Maps Terms of Service

Overview: Provides hourly pollen levels and plant-specific allergen data for a given location.

Dataset 2:

Air Quality Data

Source: Google Maps Air Quality API https://developers.google.com/maps/documentation/air-quality/overview

Creator: Google Maps Platform

Publisher: Google

License: Google API and Maps Terms of Service

Overview: Provides hourly data for air quality indices, pollutant concentrations, and health recommendations for given coordinates.


## Milestones:

Getting pollen and air quality data from the google API based on GPS

Generation of data report

Outputting report to the CLI


## Division of Labor By Week:

### 10/20 - 10/26

Domain modeling - Matti

System diagram - Jackie

Domain class diagram - Jackie

System sequence diagram - Matti

### 10/27 - 11/02

Data set of New Hampshire locations - Jackie

API requests working - Matti

### 11/03 - 11/9

Extracting information from the API requests - Jackie

Making API requests based on data set - Matti

### 11/10 - 11/16

Organization of data - Jackie

Saving allergy information - Matti

### 11/17 - 11/23

User input for allergy information - Jackie

User input for location selection - Matti

### 11/24 - 11/30

Outputing report to CLI - Matti/Jackie

### 11/30 - 12/7

Refactoring - Matti/Jackie

Debugging - Matti/Jackie

## Glossary:
API - Application Protocol Interface

Pollen - Allergen released by plants

Pollen index - Amount of pollen in a set amount of air

Location - A set location in New Hampshire

Google Maps - Online map service by Google that includes APIs for air quality and pollen

GPS - Coordinate system for geolocation

CSV - Data storage format

CLI - Command line interface

Report - Report of personalized data from the API requests

Update Allergy - Add a new allergy to the user's file

Air Quality - Index used to measure the safety and clarity of air in an area

Visual Studio Code - Coding editor used for the project

GitHub - Service used to host the projects remote repository

New Hampshire - North eastern state in the United States

Poetry - Dependency management suite for Python project

UNH - Univsersity of New Hampshire