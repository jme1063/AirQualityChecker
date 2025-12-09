| **google\_maps** | [index](.)<br>[/home/matti/SWEProjects/GroupSustainabiltyProject/projectjackiematti/src/google_maps.py](file:/home/matti/SWEProjects/GroupSustainabiltyProject/projectjackiematti/src/google_maps.py) |
| --- | --- |

##AirQuality = AIzaSyCg3\_N47a-C4c2ULomL0QgVkBLfmonNikU

| **Modules** |
| --- |
|  |  | | [csv](csv.html) | [requests](requests.html) |  |  |<br>| --- | --- | --- | --- | |

| **Classes** |
| --- |
|  |  | - [builtins.object](builtins.html#object)<br>    - - [GoogleMaps](google_maps.html#GoogleMaps)<br>
<br>
 <br><br><br><br><br>| class **GoogleMaps**([builtins.object](builtins.html#object)) |<br>| --- |<br>|  | GoogleMaps(api\_key)<br>
 <br>
Class used to send requests to the Google Maps API |<br>|  | Methods defined here:<br>
<br>- **\_\_init\_\_**(self, api\_key)<br>    - Initialize [object](builtins.html#object) attributes<br><br>

<br>- **get\_air\_quality\_info**(self, location\_name, user\_location)<br>    - Get the air quality data from the API request and saves into a dict<br>
  Arguments: String location\_name -- name of the location<br>
              UserLocation user\_location -- user location [object](builtins.html#object)<br>
              Returns: Dict with cleaned air quality data<br><br>

<br>- **get\_current\_conditions\_quality**(self, user\_location)<br>    - Get current air quality conditions for a given user location<br>
Arguments: UserLocation user\_location -- user location [object](builtins.html#object)<br>
Returns: JSON data from the API request<br><br>

<br>- **get\_forecast\_pollen**(self, user\_location)<br>    - Get forecasted pollen levels for a given user location<br>
Arguments: UserLocation user\_location -- user location [object](builtins.html#object)<br>
Returns: JSON data from the API request<br><br>

<br>- **get\_pollen\_info**(self, location\_name, user\_location)<br>    - Gets the pollen data from the API request and stores in a dict<br>
Arguments: String location\_name -- name of the location<br>
           UserLocation user\_location -- user location [object](builtins.html#object)<br>
Returns: Dict with cleaned pollen data<br><br>

<br>- **save\_to\_csv**(self, user\_location)<br>    - Get data extracted from pollen and air quality functions<br>
and save to CSV<br>
Arguments: UserLocation user\_location -- user location [object](builtins.html#object)<br><br>

<br>* * *<br>
Data descriptors defined here:<br>
<br>- **\_\_dict\_\_**<br>
    - dictionary for instance variables<br>
<br>
<br>- **\_\_weakref\_\_**<br>
    - list of weak references to the object | |