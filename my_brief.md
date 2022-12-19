Patient Management App
The infamous Arkham Asylum in Gotham City has approached you to build a web application to help them manage their patients and doctors. A doctor may look after MANY patients at a time. A patient is assigned only ONE doctor and ONE officer/vigilante.

MVP
The asylum wants to be able to register / track patients. Important information for the asylum to know is -
Name
Date Of Birth (use a VARCHAR initially)
Type of patient (human/non-human)
Enhanced (true/false)
Details for arresting vigilante/officer
Treatment notes
Be able to assign patients to doctors
CRUD actions for doctors / patients - remember the user - what would they want to see on each View? What Views should there be?

Possible Extensions
If an officer/vigilante has multiple patients we don't want to keep updating contact details separately for each patient. Extend your application to reflect that an officer/vigilante can have MANY patients and to more sensibly keep track of officer/vigilantes' details (avoiding repetition / inconsistencies)
Handle check-in / check-out dates
Let the asylum see all patients currently in the asylum (today's date is between the check-in and check-out?)
Sometimes an officer/vigilante does not know the DOB. Allow them to enter an age instead. Try and make sure this always up to date - ie if they visit again a year from now a 3 yr old dog is now 4.
Add extra functionality of your choosing - assigning treatments, a more comprehensive way of maintaining treatment notes over time.