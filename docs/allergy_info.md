| **allergy\_info** | [index](.)<br>[/home/matti/SWEProjects/GroupSustainabiltyProject/projectjackiematti/src/allergy_info.py](file:/home/matti/SWEProjects/GroupSustainabiltyProject/projectjackiematti/src/allergy_info.py) |
| --- | --- |

| **Modules** |
| --- |
|  |  | | [csv](csv.html) |  |  |  |<br>| --- | --- | --- | --- | |

| **Classes** |
| --- |
|  |  | - [builtins.object](builtins.html#object)<br>    - - [AllergyInfo](allergy_info.html#AllergyInfo)<br>
<br>
 <br><br><br><br><br>| class **AllergyInfo**([builtins.object](builtins.html#object)) |<br>| --- |<br>|  | Class to manage allergy information for users |<br>|  | Methods defined here:<br>
<br>- **\_\_init\_\_**(self)<br>    - Constructor for AllergyInfo class<br><br>

<br>- **add\_new\_user**(self, name)<br>    - Adds a new user without any allergies<br>
Arguments: String name -- name of the user<br><br>

<br>- **add\_new\_user\_with\_allergy**(self, name, allergy\_list)<br>    - Adds a new user with an initial allergy list<br>
Arguments: String name -- name of the user<br>
           String allergy\_list -- list of allergies in string format<br><br>

<br>- **get\_allergy\_info**(self, name)<br>    - Retrieves the allergy information for a user<br>
Arguments: String name -- name of the user<br><br>

<br>- **update\_allergy**(self, name, allergy)<br>    - Updates the allergy information for a user by adding a new allergy.<br>
Arguments: String name -- name of the user<br>
           String -- allergy to be added<br><br>

<br>* * *<br>
Data descriptors defined here:<br>
<br>- **\_\_dict\_\_**<br>
    - dictionary for instance variables<br>
<br>
<br>- **\_\_weakref\_\_**<br>
    - list of weak references to the object | |