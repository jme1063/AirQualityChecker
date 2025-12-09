| **app** | [index](.)<br>[/home/matti/SWEProjects/GroupSustainabiltyProject/projectjackiematti/src/app.py](file:/home/matti/SWEProjects/GroupSustainabiltyProject/projectjackiematti/src/app.py) |
| --- | --- |

| **Modules** |
| --- |
|  |  | | [csv](csv.html) | [os](os.html) |  |  |<br>| --- | --- | --- | --- | |

| **Classes** |
| --- |
|  |  | - [builtins.object](builtins.html#object)<br>    - - [App](app.html#App)<br>
<br>
 <br><br><br><br><br>| class **App**([builtins.object](builtins.html#object)) |<br>| --- |<br>|  | App(maps\_api, allergy\_info\_obj, name)<br>
 <br>
Main interface between main and the domain model classes |<br>|  | Methods defined here:<br>
<br>- **\_\_init\_\_**(self, maps\_api, allergy\_info\_obj, name)<br>    - Constructor that takes in a google\_maps [object](builtins.html#object), allergy\_info [object](builtins.html#object), and user name<br>
Arguements: GoogleMaps maps\_api -- google maps api [object](builtins.html#object)<br>
            AllergyInfo allergy\_info\_obj -- allergy info [object](builtins.html#object)<br>
            String name -- name of the user<br><br>

<br>- **add\_allergy\_info**(self, allergy)<br>    - Adds allergy information for the user with an allergy string as input<br>
Arguments: String allergy -- allergy to be added<br><br>

<br>- **fetch\_air\_data**(self)<br>    - Fetches air quality data for the user's location using the google\_maps [object](builtins.html#object)<br><br>

<br>- **generate\_report**(self, csv\_path='data/report.csv')<br>    - Generates a report using organized data from data\_organizer, prints it, and writes it to a CSV file.<br><br>

<br>- **get\_allergy\_info**(self)<br>    - Gets the allergy information for the user<br>
Returns: List of allergies for the user<br><br>

<br>- **set\_user\_location**(self, location)<br>    - Sets the user location based on a location name<br>
Arguments: String location -- name of the location<br><br>

<br>* * *<br>
Data descriptors defined here:<br>
<br>- **\_\_dict\_\_**<br>
    - dictionary for instance variables<br>
<br>
<br>- **\_\_weakref\_\_**<br>
    - list of weak references to the object | |