"""
testUserLocation.py - Unit tests for UserLocation class
Tests the userLocation.py program stored in the src directory.
Prints out object information for all location objects created.
"""

import unittest
import sys
import os

# Add the src directory to the path so we can import userLocation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from user_location import UserLocation


class TestUserLocation(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_lat = 42.9956
        self.test_lon = -71.4548
        self.test_name = "Manchester"
        self.user_location = UserLocation(self.test_lat, self.test_lon, self.test_name)
    
    def print_object_info(self, location, title="Location Object Info"):
        """Helper method to print detailed object information."""
        print(f"\n--- {title} ---")
        print(f"Name: {location.name}")
        print(f"Latitude: {location.latitude}")
        print(f"Longitude: {location.longitude}")
        print(f"String representation: {str(location)}")
        print("-" * (len(title) + 8))
    
    def test_init_and_print_info(self):
        """Test UserLocation initialization and print object information."""
        print("\n" + "="*60)
        print("TEST: UserLocation Initialization")
        print("="*60)
        
        # Test the setUp location
        self.print_object_info(self.user_location, "Manchester Location (from setUp)")
        
        # Verify the attributes are set correctly
        self.assertEqual(self.user_location.latitude, self.test_lat)
        self.assertEqual(self.user_location.longitude, self.test_lon)
        self.assertEqual(self.user_location.name, self.test_name)
        
        print("✓ Initialization test passed!")
    
    def test_create_multiple_locations_and_print(self):
        """
        Test creating multiple location objects and print all their information.
        This demonstrates creating various NH locations.
        """
        print("\n" + "="*60)
        print("TEST: Creating Multiple NH Location Objects")
        print("="*60)
        
        # Create multiple NH locations
        locations = [
            UserLocation(42.9956, -71.4548, "Manchester"),
            UserLocation(43.2081, -71.5376, "Concord"),
            UserLocation(43.0718, -70.7626, "Portsmouth"),
            UserLocation(42.7654, -71.4676, "Nashua"),
            UserLocation(43.1979, -70.8737, "Dover")
        ]
        
        print(f"Created {len(locations)} UserLocation objects:")
        
        # Print information for each location
        for i, location in enumerate(locations, 1):
            self.print_object_info(location, f"Location #{i}: {location.name}")
            
            # Verify each location has valid data
            self.assertIsInstance(location.latitude, (int, float))
            self.assertIsInstance(location.longitude, (int, float))
            self.assertIsInstance(location.name, str)
            self.assertTrue(location.name)  # Name should not be empty
        
        print(f"✓ Successfully created and verified {len(locations)} location objects!")
        return locations
    

    
    def test_string_representations_and_print(self):
        """Test string representation (__str__) and print examples."""
        print("\n" + "="*60)
        print("TEST: String Representation")
        print("="*60)
        
        # Create test locations with different characteristics
        test_locations = [
            UserLocation(42.8651, -71.4990, "Merrimack"),
            UserLocation(43.3767, -72.3465, "Claremont"),
            UserLocation(0.0, 0.0, "Test Zero Coordinates"),
            UserLocation(-42.5, 171.2, "Test Negative Coordinates")
        ]
        
        for i, location in enumerate(test_locations, 1):
            print(f"\nLocation {i}: Testing string representation")
            print(f"  Name: {location.name}")
            print(f"  Coordinates: ({location.latitude}, {location.longitude})")
            print(f"  str() result: '{str(location)}'")
            
            # Verify string representation contains expected information
            str_repr = str(location)
            
            self.assertIn(location.name, str_repr)
            self.assertIn(str(location.latitude), str_repr)
            self.assertIn(str(location.longitude), str_repr)
        
        print("✓ String representation test passed!")
    
    def test_comprehensive_object_demo(self):
        """
        Comprehensive demonstration of all UserLocation object capabilities.
        Creates various objects and prints all their information.
        """
        print("\n" + "="*70)
        print("COMPREHENSIVE DEMO: All UserLocation Object Information")
        print("="*70)
        
        # Create a variety of locations to demonstrate different scenarios
        demo_locations = [
            # Major NH cities
            UserLocation(42.9956, -71.4548, "Manchester"),
            UserLocation(43.2081, -71.5376, "Concord"),
            UserLocation(43.0718, -70.7626, "Portsmouth"),
            UserLocation(42.7654, -71.4676, "Nashua"),
            
            # Edge cases
            UserLocation(44.0, -71.0, "Northern NH Location"),
            UserLocation(42.5, -70.5, "Southeastern NH Location")
        ]
        
        print(f"Demonstrating {len(demo_locations)} UserLocation objects:\n")
        
        for i, location in enumerate(demo_locations, 1):
            print(f"{'='*20} OBJECT #{i} {'='*20}")
            self.print_object_info(location, f"Demo Object #{i}")
            
            # Verify object attributes
            self.assertIsInstance(location.latitude, (int, float))
            self.assertIsInstance(location.longitude, (int, float))
            self.assertIsInstance(location.name, str)
            self.assertTrue(location.name)  # Name should not be empty
            
            print("✓ Object verification successful!")
            print()
        
        print("="*70)
        print(f"✓ DEMO COMPLETE: All {len(demo_locations)} objects created and verified successfully!")
        print("="*70)
        
        return demo_locations
    
    def test_csv_functionality_and_print(self):
        """
        Test CSV loading functionality and print information for all loaded locations.
        This loads the actual NH locations from the CSV file.
        """
        print("\n" + "="*60)
        print("TEST: Loading UserLocation Objects from CSV File")
        print("="*60)
        
        # Path to the CSV file
        csv_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'nh_locations.csv')
        print(f"Loading locations from: {csv_file_path}")
        
        # Load locations from CSV
        locations = UserLocation.load_from_csv(csv_file_path)
        
        if not locations:
            print("⚠️ Warning: No locations loaded from CSV file")
            return
        
        print(f"\n✓ Successfully loaded {len(locations)} locations from CSV!")
        print(f"Printing information for all {len(locations)} location objects:\n")
        
        # Print information for each loaded location
        for i, location in enumerate(locations, 1):
            self.print_object_info(location, f"CSV Location #{i}: {location.name}")
            
            # Verify each location has valid data
            self.assertIsInstance(location.latitude, (int, float))
            self.assertIsInstance(location.longitude, (int, float))
            self.assertIsInstance(location.name, str)
            self.assertTrue(location.name)  # Name should not be empty
            
            # Verify coordinates are reasonable for New Hampshire
            self.assertTrue(41.0 < location.latitude < 46.0)  # NH latitude range
            self.assertTrue(-73.0 < location.longitude < -70.0)  # NH longitude range
        
        print(f"✓ All {len(locations)} CSV locations verified successfully!")
        return locations
    
    def test_csv_row_creation_and_print(self):
        """
        Test creating UserLocation from CSV row format and print information.
        """
        print("\n" + "="*60)
        print("TEST: Creating UserLocation from CSV Row Data")
        print("="*60)
        
        # Sample CSV row data (like what comes from csv.DictReader)
        csv_rows = [
            {
                'name': 'Test Manchester',
                'latitude': '42.9956',
                'longitude': '-71.4548',
                'type': 'city',
                'county': 'Hillsborough'
            },
            {
                'name': 'Test Concord',
                'latitude': '43.2081',
                'longitude': '-71.5376',
                'type': 'city',
                'county': 'Merrimack'
            }
        ]
        
        created_locations = []
        
        for i, row_data in enumerate(csv_rows, 1):
            print(f"\nCreating location {i} from CSV row:")
            print(f"Input CSV row: {row_data}")
            
            location = UserLocation.from_csv_row(row_data)
            created_locations.append(location)
            
            self.print_object_info(location, f"Created from CSV Row: {location.name}")
            
            # Verify the location was created correctly
            self.assertEqual(location.latitude, float(row_data['latitude']))
            self.assertEqual(location.longitude, float(row_data['longitude']))
            self.assertEqual(location.name, row_data['name'])
        
        print(f"✓ Successfully created and verified {len(created_locations)} locations from CSV rows!")
        return created_locations


if __name__ == '__main__':
    print("="*80)
    print("UserLocation Class - Unit Tests with Object Information Display")
    print("="*80)
    print("This test suite will create various UserLocation objects and")
    print("print detailed information about each object created.")
    print("="*80)
    
    # Run the tests with verbose output
    unittest.main(verbosity=2)
