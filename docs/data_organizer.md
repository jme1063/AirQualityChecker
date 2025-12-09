| **data\_organizer** | [index](.)<br>[/home/matti/SWEProjects/GroupSustainabiltyProject/projectjackiematti/src/data_organizer.py](file:/home/matti/SWEProjects/GroupSustainabiltyProject/projectjackiematti/src/data_organizer.py) |
| --- | --- |

Organizes API data for easy extraction of plant species and air quality.

- Returns a list of all plant species (plantType)

- Returns a string of the latest air quality (airQuality)

- Organizes a CSV file so only the latest entry is kept. This is so we can reference

  older information still while organizing current information from the API requests.

| **Modules** |
| --- |
|  |  | | [csv](csv.html) | [os](os.html) |  |  |<br>| --- | --- | --- | --- | |

| **Classes** |
| --- |
|  |  | - [builtins.object](builtins.html#object)<br>    - - [DataOrganizer](data_organizer.html#DataOrganizer)<br>
<br>
 <br><br><br><br><br>| class **DataOrganizer**([builtins.object](builtins.html#object)) |<br>| --- |<br>|  |  | Methods defined here:<br>
<br>- **\_\_init\_\_**(self)<br>    - Initializes the data\_organizer [object](builtins.html#object) by setting up file paths for input and output CSV files.<br><br>

<br>- **get\_air\_quality**(self)<br>    - Reads the input CSV and returns the latest air quality string found.<br><br>

<br>- **get\_all\_plant\_species**(self)<br>    - Reads the input CSV and returns a sorted list of all unique plant species found.<br><br>

<br>- **get\_all\_pollen\_types**(self)<br>    - Reads the input CSV and returns a sorted list of all unique pollen types found.<br><br>

<br>- **return\_all\_info**(self)<br>    - Organizes the data, then returns the list of plant species, the latest air quality info, and the list of pollen types.<br>
Returns: tuple (plant\_type: list of strings, air\_quality: string or None, pollen\_type: list of strings)<br><br>

<br>- **sort\_csv\_file**(self)<br>    - Reads the input CSV, keeping only the latest (last) entry, and writes organized data to the output CSV.<br>
The output includes city info, air quality, pollen types, and plant species, each under their own heading<br>
to make it easier to reference later.<br><br>

<br>* * *<br>
Data descriptors defined here:<br>
<br>- **\_\_dict\_\_**<br>
    - dictionary for instance variables<br>
<br>
<br>- **\_\_weakref\_\_**<br>
    - list of weak references to the object | |