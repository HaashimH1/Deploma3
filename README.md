# Gym face

A Python based terminal web appliaction to manage customer data. Using google sheets as the database, connected to it with its API, this program offers admin members of a gym to access the database of customers data qucikly and effectivly to update, remove and add customers or their data, making this a versatile solution for gym owners looking to integrate a admin interface for workers to access.

Live website can be found [Here](https://deploma3-62c85e28efa9.herokuapp.com/)

## Table of Contents

placeholder

## User Expectations

This program is made to be used by staff members for a gym, so they would typically be trained to use this program, however I have made it easy to use with no training provided.

Users expect to :

- Access the datbase held in the google sheet to display, add, update or remove data quickly and effectivly to help the business strive
- All data displayed is easy to read, with different apects of the data having distinctive features to help first timer users understand it as a whole.
- Fast data manipluation, with any changes made being swiftly shown in the spreadsheet
- Least key inputs as possible for increased effieciency within work environment

## Google Sheets

There are 2 sheets that holds all data

- Profiles sheet Holds all personal customer data in these fields:
  - First Name
  - Last Name
  - Email Address
  - Phone number
  - Date of Birth
- History sheet : Holds all Gym realted data in these fields:
  - Signup Date
  - Payment Entrys (In the Form of [payment amount,payment date] seperated by '|')
  - Visits Entrys (Each visits date seperated by '|')
  - Enddate (Subscription End date, this is defaulted as signup date when profile created)

The subscription 'Active' status is a field that only appears when using the program and is not stored in the sheets themselves. This is because the program needs to determine whether the customers subcription is active based on their enddate, if this was stored in the sheet i would need to have the sheet being automaticlly updated using a server or manually do it myself in time intervals which is way beyond the scope of this project, therefore a simple alternative is for it to only be seen in the program.

Below are snippets of what the sheets look like:

- ![sad](/README_assets/doc_14.png)
- ![dfgdf](/README_assets/doc_15.png)

## Program / Features Walkthrough

Whole program is contained in a terminal window, 80 x 24 characters wide and long.

### Program Start

![first lauching the terminal](/README_assets/doc_1.png)

- Upon launching the program, it first sets up the connections to the Google spreadsheet, giving a message 'setting up..'
- Also on the website there is a button 'RUN PROGRAM' which can start or restart the program.

### Main Menu

![main menu](/README_assets/doc_2.png)

- Upon setup completion the main menu is displayed, showing 6 different options to choose from.

  1. See All data
  2. Create a Profile
  3. Edit a Profile
  4. Log a Visit
  5. Make a Payment
  6. Delete a Profile

### Option 1: See all Data

![profile table](/README_assets/doc_3.png)

- Shows all profiles from the sheet in a organsied and colour coded table.

![hitory table](/README_assets/doc_4.png)

- User input an ID to select a certain profile to show its history in a organised colour coded table.
- Then a prompt to press any key to return to main menu

### Option 2: Create a Pofile

![creating a profile](/README_assets/doc_5.png)

- User is walked through on how to create the profile, inputing each field and alsi validated:
  - First and Last Name: At least 2 characters, only letters A-Z allows
  - Email: Standard Email format
  - Phone number: UK number format of 447XXXXXXXXX
  - Date of Birth: UK date format of DD/MM/YYYY
- After all this is input and validated to make sure its in formats, previews the profile with its data then updates the Google sheet adding the new

### Option 3: Edit a Profile

![searching for profile](/README_assets/doc_6.png)

- User enters a search field to find a profile and select it by its ID.

![editing profile](/README_assets/doc_7.png)

- Previews the profile then user chooses which field to change and inputs new field data, this is looped untill option 6 is chosen to save the changes.

![saving changes](/README_assets/doc_8.png)

- Previews profile with its final data then updates the Google sheet accordingly.
- Return to meny prompt

### Option 4: Log a Visit

![logging a visit](/README_assets/doc_9.png)

- User seraches and selects a Profile the same way as shown in [Option 3: Edit a Profile](#option-3-edit-a-profile).
- Then if profile has an active subscription and has not already logged today, then adds a visit entry to history sheet.

### Option 5: Make a Payment

![searching profile and displaying package options](/README_assets/doc_10.png)

- User seraches and selects a Profile the same way as shown in [Option 3: Edit a Profile](#option-3-edit-a-profile).
- User then selects which subscription package the customer has paid for.

![choosing package option](/README_assets/doc_11.png)

- Payment entry is added to sheet and subscription enddate updated/extended
- Return to menu prompt

### Option 6: Delete a Profile

![confirming profile deletion](/README_assets/doc_12.png)

- User seraches and selects a Profile the same way as shown in [Option 3: Edit a Profile](#option-3-edit-a-profile).
- Must write 'confirm' in any case as this is a permanent deletion

![profile deleted](/README_assets/doc_13.png)

- Profile is then removed from both sheets after confirmation
- Return to main menu prompt

## Implementation

This section will go in depth on how all the features were implemented down to the code.

But firstly we need to cover the file structure of 3 python files and their purposes:
  - run.py -> Main Program Functions
  - validator.py -> Validate user inputs
  - sheets.py -> Set and Get data to/from the Google SpreadSheet

![Class Diagram](/README_assets/doc_16.png)

- Instances for both Validator and GoogleSheets are in run.py as this is the main file where all the program functions are so its objects methods are used to organise and increase reusabilty within the code.
