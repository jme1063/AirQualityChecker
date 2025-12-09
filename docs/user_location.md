| **user\_location** | [index](.)<br>[/home/matti/SWEProjects/GroupSustainabiltyProject/projectjackiematti/src/user_location.py](file:/home/matti/SWEProjects/GroupSustainabiltyProject/projectjackiematti/src/user_location.py) |
| --- | --- |

userLocation.py - Implementation of userLocation class from domain model

| **Modules** |
| --- |
|  |  | | [csv](csv.html) |  |  |  |<br>| --- | --- | --- | --- | |

| **Classes** |
| --- |
|  |  | - [builtins.object](builtins.html#object)<br>    - - [UserLocation](user_location.html#UserLocation)<br>
<br>
 <br><br><br><br><br>| class **UserLocation**([builtins.object](builtins.html#object)) |<br>| --- |<br>|  | UserLocation(latitude: float, longitude: float, name: str)<br>
 <br>
Represents a geographical location with coordinates and name. |<br>|  | Methods defined here:<br>
<br>- **\_\_init\_\_**(self, latitude: float, longitude: float, name: str)<br>    - initialize [object](builtins.html#object) attributes<br><br>

<br>- **\_\_str\_\_**(self)<br>    - Currently combines [object](builtins.html#object) attributes and returns it in string format.<br><br>

<br>* * *<br>
Class methods defined here:<br>
<br>- **from\_csv\_row**(row\_data: dict)<br>    - Pulls information from the manually created location dataset and creates userLocation based<br>
off of the name the user gave<br>
Expects a dictionary with keys: name, latitude, longitude<br><br>

<br>- **load\_from\_csv**(csv\_file\_path: str)<br>    - Load all user\_location objects from a CSV file.<br>
Returns a list of user\_location objects.<br><br>

<br>* * *<br>
Data descriptors defined here:<br>
<br>- **\_\_dict\_\_**<br>
    - dictionary for instance variables<br>
<br>
<br>- **\_\_weakref\_\_**<br>
    - list of weak references to the object | |