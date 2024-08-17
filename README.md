# Gym face

A Python based terminal web appliaction to manage customer data. Using google sheets as the database, connected to it with its API, this program offers admin members of a gym to access the database of customers data qucikly and effectivly to update, remove and add customers or their data, making this a versatile solution for gym owners looking to integrate a admin interface for workers to access.

Live website can be found [Here](https://deploma3-62c85e28efa9.herokuapp.com/)

## Table of Contents

- [Gym face](#gym-face)
- [User Expectations](#user-expectations)
- [Google Sheets](#google-sheets)
- [Program / Features Walkthrough](#program--features-walkthrough)
  - [Program Start](#program-start)
  - [Main Menu](#main-menu)
  - [Option 1: See all Data](#option-1-see-all-data)
  - [Option 2: Create a Profile](#option-2-create-a-profile)
  - [Option 3: Edit a Profile](#option-3-edit-a-profile)
  - [Option 4: Log a Visit](#option-4-log-a-visit)
  - [Option 5: Make a Payment](#option-5-make-a-payment)
  - [Option 6: Delete a Profile](#option-6-delete-a-profile)
- [Implementation](#implementation)
  - [File/Class Structure](#fileclass-structure)
  - [Settup](#settup)
  - [Menu](#menu)
  - [See All Data](#see-all-data)
  - [Create a Profile](#create-a-profile)
  - [Edit a Profile](#edit-a-profile)
  - [Log A Visit](#log-a-visit)
  - [Make a Payment](#make-a-payment)
  - [Delete a Profile](#delete-a-profile)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [CI Python Linter Validation (PEP8)](#ci-python-linter-validation-pep8)
  - [Testing](#testing-1)
- [Deployment](#deployment)
  - [Google Sheets Setup](#google-sheets-setup)
  - [GitHub Repository Setup](#github-repository-setup)
  - [Deployment to Heroku](#deployment-to-heroku)
- [Credits](#credits)


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

`** NOTE ** - Any use of the return to menu prompt 'Press ANY KEY' has been changed to 'Press ENTER' to better represent its actual functionality` 

Whole program is contained in a terminal window, 80 x 24 characters wide and long.

### Program Start

![first lauching the terminal](/README_assets/doc_1.png)

- Upon launching the program, it first sets up the connections to the Google spreadsheet, giving a message 'setting up..'
- Also on the website there is a button 'RUN PROGRAM' which can start or restart the program.

### Main Menu

![main menu](/README_assets/doc_2.png)

Upon setup completion the main menu is displayed, showing 6 different options to choose from.

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

### File/Class Structure

But firstly we need to cover the file structure of 3 python files and their purposes:

- run.py -> Main Program Functions
- validator.py -> Validate user inputs
- sheets.py -> Set and Get data to/from the Google SpreadSheet

![Class Diagram](/README_assets/doc_16.png)

- Instances for both Validator and GoogleSheets are in run.py as this is the main file where all the program functions are so its objects methods are used to organise and increase reusabilty within the code.

### Settup

The very first function that is called is main in run.py

```python
if __name__ == "__main__":
    main()
```

- A condition to only run the program if the script is run from run.py, running the script using sheets/validator.py will not call the fucntion main

Below is the global variables that will be used all over this file.

```python
# All global variables
gsheet = None
valid = None

# colour codes for printing to terminal
BLACK = "\033[30m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
WHITE = "\033[97m"
RESET_COLOUR = "\033[0m"

# each field is asigned a colour
BORDER_COLOUR = WHITE
ID_COLOUR = RED
FNAME_COLOUR = GREEN
LNAME_COLOUR = GREEN
EMAIL_COLOUR = YELLOW
PHONE_COLOUR = PURPLE
DOB_COLOUR = BLUE

# subscription pricings
PAYMENT_AMOUNT_1MONTH = 29.99
PAYMENT_AMOUNT_3MONTH = 79.99
PAYMENT_AMOUNT_6MONTH = 149.99
PAYMENT_AMOUNT_9MONTH = 219.99
PAYMENT_AMOUNT_12MONTH = 249.99
```

- Declaring objects so it can be accessed anywhere in this file.
- ANSI colour codes for displaying different coloured texts to terminal to show differentiation between fields and focus on certain aspects.
- Subscription pricings so it can be easily updated without digging deep into code, as pricings are very volatile for a business.

```python
def main():
    print(f"{GREEN}    Setting up...")
    global gsheet
    global valid
    gsheet = GoogleSheets()
    valid = Validator(RED,RESET_COLOUR)

    main_menu()
```

- Initializes the objects which will setup each by its `__init__` methods, all messages that are printed to the terminal are mostly used by F strings as it is very easy to insert the colour code desired and its message, after the objects are initialized main_menu is displayed.

Below are the `__init__` methods from both classes

```python
# Global var for custom data to access google sheet as may be updated
SPREADSHEET_NAME = "Deploma3"
SHEET_NAME1 = "Profile"
SHEET_NAME2 = "History"
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

class GoogleSheets:
    def __init__(self):
        self.CREDS = Credentials.from_service_account_file("creds.json")
        self.SCOPED_CREDS = self.CREDS.with_scopes(SCOPE)
        self.GSPREAD_CLIENT = gspread.authorize(self.SCOPED_CREDS)
        self.SHEET = self.GSPREAD_CLIENT.open(SPREADSHEET_NAME)
        self.profiles = self.SHEET.worksheet(SHEET_NAME1)
        self.history = self.SHEET.worksheet(SHEET_NAME2)
```

- Setups the API to the both sheets

```python
class Validator:
    def __init__(self,ERROR_COLOUR,RESET_COLOUR):
        self.ERROR_COLOUR = ERROR_COLOUR
        self.RESET_COLOUR = RESET_COLOUR
```

- Not much going on, just sets the colour code attributes that this file would need

### Menu

```python
def main_menu():

    clear_terminal()

    print(logo) # logo is a string of ascii characters that makes up the Gym face logo
    print(f"\n                                   {PURPLE}Main Menu\n                               {GREEN}Choose an Option:\n")
    print(f"   {BLUE}1 {WHITE}--> See all Data    {BLUE}2 {WHITE}--> Create a Profile  {BLUE}3 {WHITE}--> Edit a Profile\n")
    print(f"   {BLUE}4 {WHITE}--> Log a Visit     {BLUE}5 {WHITE}--> Make a Payment    {BLUE}6 {WHITE}--> Delete a Profile\n")

    option = get_user_input("Option",valid.validate_option,BLUE,[1,2,3,4,5,6])
    option = int(option)

    if option == 1:
        see_all_data()
    elif option == 2:
        create_a_profile()
    elif option == 3:
        edit_a_profile()
    elif option == 4:
        log_a_visit()
    elif option == 5:
        make_a_payment()
    elif option == 6:
        delete_a_profile()
```

- Firstly, the terminal is cleared using a custom function
- Then after displaying the menu option to user, a function `get_user_input()` is used to obtain the input of the user and make sure it is validated.
- Function is called respective to menu option chosen

The `get_user_input()` function will be used countless times throughout this program so below is how it works:

```python
def get_user_input(field,validate_function,colour,options = []):

    while True:
        user_input = input(f"{WHITE}Please enter a {colour}{field}{WHITE}, or type '{PURPLE}menu{WHITE}' to go back to main menu >{RESET_COLOUR} \n")
        if user_input.lower() == "menu":
            main_menu()
        else:
            if options:
                if validate_function(user_input,options,field):
                    return user_input
            else:
                if validate_function(user_input,field):
                    return user_input
```

- There are 4 parameters
  - `field`: the field of the input (example: email)
  - `validate_function`: the function held in validator.py that will validate this specific field
  - `colour`: colour to display as the field
  - `options`: if the input is to choose an option, a list of integers are passed in

1. **Input Prompt**:

   - The user is prompted to enter a value for the specified `field`. The prompt includes an option to type 'menu' to return to the main menu.

2. **Main Menu Navigation**:

   - If the user types 'menu' (non case-insensitive), the function calls `main_menu()` to navigate back to the main menu.

3. **Input Validation**:
   - If `options` is provided (i.e., not empty), the `validate_function` is called with `user_input`, `options`, and `field` as arguments.
   - If `options` is empty, the `validate_function` is called with only `user_input` and `field` as arguments.
   - If the `validate_function` returns `True`, indicating valid input, the function returns `user_input`.
   - If the input is invalid, the loop continues until the user provides valid input or chooses to return to the main menu.

For example This will get the user to choose an option in the main menu:

```python
option = get_user_input("Option",valid.validate_option,BLUE,[1,2,3,4,5,6])
```

- `Option` is the field as the use is choosing an 'Option' to choose from
- `valid.validate_option` is the valids object method to handle this specific input
- `BLUE` is the colour to display this field as
- `[1,2,3,4,5,6]` Menu options are passed in as this is a option type, so this is also passed into the validate function

Another Example, user is needs to input a Email Address

```python
email = get_user_input("Email Address",valid.validate_email,EMAIL_COLOUR)
```

- `Email Address` is the field as the use is inputting a Email
- `valid.validate_email` is the valids object method to handle this specific input
- `EMAIL_COLOUR` is the colour to display this field as
- No List of integers were passed in so the when calling the validate function it does not include `options = []` as its an empty list

Below is the function in validator.py that will validate the input for menu options:

```python
def validate_option(self,user_option,all_options,field):
        try:
            if int(user_option) in all_options:
                return True
            else:
                self.print_to_terminal(field,f"be {all_options}")
                return False
        except:
            self.print_to_terminal(field,"be a number")
            return False
```

- function `print_to_terminal()` just takes in error reasons and displays them to user in a reusable format.

### See All Data

```python
def see_all_data():
    clear_terminal()
    print(f"\n\n                   {GREEN}Getting all Profiles....\n")
    print_profile_table(gsheet.get_all_profile_data())
    print(f"{WHITE}To show the history of a customer:\n")
    Id = get_user_input_id()
    print(f"{GREEN}           Getting {ID_COLOUR}{Id}{GREEN}'s history data....")
    print_history_table(gsheet.get_history_data(int(Id)))
    return_to_main_menu_prompt()
```

- Clears terminal.
- Retrieves all data in Profiles sheet and displays in a colour coded and organised table.
- Then user enters a ID to see its history data in a organised table, the fucntion `get_user_input_id()` essentially uses the function we used for inputs before but also checks if the given ID exists in the database.
- `return_to_main_menu_prompt()` just displays to user "Pres any key to return to menu", to which after a key is pressed it calls `main_menu()` to load the main menu again

### Create a Profile

```python
def create_a_profile():
    clear_terminal()
    firstname = get_user_input("First Name",valid.validate_name,FNAME_COLOUR)
    lastname = get_user_input("last Name",valid.validate_name,LNAME_COLOUR)
    email = get_user_input("Email Address",valid.validate_email,EMAIL_COLOUR)
    phone = get_user_input("Phone Number",valid.validate_phone,PHONE_COLOUR)
    dob = get_user_input("Date of Birth",valid.validate_dob,DOB_COLOUR)

    Id = len(gsheet.get_all_profile_data())

    new_row = [str(Id),firstname,lastname,email,str(phone),dob]
    print_preview_profile(new_row)
    gsheet.add_new_profile(new_row,Id,valid.get_todays_date())
    print(f"\n{GREEN}         New Pofile succesfully added to database")
    return_to_main_menu_prompt()
```

- Clears terminal
- 5 fields need to be input by user, passing `get_user_input()` its respective field name, validating function and colour to display the firld as. Below are the requirments to pass validation for each field:
  - First/Last Name: Only letters, at least 2 characters long
  - Email Address: Regex pattern of `'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'`
  - Phone Number: Regex pattern of `'^447\d{9}$'`
  - Date of Birth: Regex pattern of `'^[0-9]{2}/[0-9]{2}/[0-9]{4}$'`, a real date and has to be before today.
- Then an ID is created by getting the current amount of profiles in the .
- Shows a preview of the new profile in a table with its data using `print_preview_profile()` passing in a list the profiles data.
- Then using a function in sheets.py `add_new_profile()` which handles updating the sheets to add the new profile.
- return to main menu prompt

### Edit a Profile

```python
def edit_a_profile():

    clear_terminal()
    search_for_a_profile()
    Id = int(get_user_input_id())
    data = gsheet.get_all_profile_data()[Id]

    clear_terminal()

    confirm_changes = False

    while not confirm_changes:

        print_preview_profile(data)

        print(f"{WHITE}Now choose wahat field to change (example: 2) >\n")
        print(f"                {RED}1{WHITE} -> {FNAME_COLOUR}firstname")
        print(f"                {RED}2{WHITE} -> {LNAME_COLOUR}lastname")
        print(f"                {RED}3{WHITE} -> {EMAIL_COLOUR}email")
        print(f"                {RED}4{WHITE} -> {PHONE_COLOUR}phone number")
        print(f"                {RED}5{WHITE} -> {DOB_COLOUR}date of birth")
        print(f"                {RED}6{WHITE} -> {ID_COLOUR}CONFIRM AND SET CHANGES")

        option = int(get_user_input("Option",valid.validate_option,BLUE,[1,2,3,4,5,6]))

        if option == 1:
            fname = get_user_input("Name",valid.validate_name,FNAME_COLOUR)
            data[1] = fname
        elif option == 2:
            lname = get_user_input("Name",valid.validate_name,LNAME_COLOUR)
            data[2] = lname
        elif option == 3:
            email = get_user_input("Email Address",valid.validate_email,EMAIL_COLOUR)
            data[3] = email
        elif option == 4:
            phone = get_user_input("Phone Number",valid.validate_phone,PHONE_COLOUR)
            data[4] = phone
        elif option == 5:
            dob = get_user_input("Date Of Birth",valid.validate_dob,DOB_COLOUR)
            data[5] = dob
        elif option == 6:
            confirm_changes = True

    clear_terminal()
    print_preview_profile(data)
    gsheet.update_profile(data)
    print(f"{GREEN} Profile updated")
    return_to_main_menu_prompt()
```

- Clears terminal.
- `search_for_a_profile()` is function where it takes a user inputed search criteria, searches through every item in profiles sheet to find matching profiles, then displays which profiles were found in a preview table.
- User inputs the ID they would like to select using the same `get_user_input_id()` function.
- `data` variable is a list containing the selected profiles data, this would then be updated and validated in a loop untill the user has chosen to set changes which will break the while loop.
- When while loop is broken, previews final `data` list one last time to user, then uses a function in sheets.py `update_profile(data)` which takes in a list of the new profiles data, this function handles updating the apropriate profile with its new fields.
- return to main menu prompt.

### Log A Visit

```python
def log_a_visit():
    clear_terminal()
    search_for_a_profile()
    Id = int(get_user_input_id())
    data = gsheet.get_history_data(Id)

    if not is_user_active(data[4]):
        print(f"{RED}User is not subscribed{RESET_COLOUR}")
    elif check_user_logged_today(data[3]):
        print(f"{RED}User has already logged today{RESET_COLOUR}")
    else:
        gsheet.add_visit(valid.get_todays_date(),Id,data[3])
        print(f"{GREEN}        Logged Users Visit{RESET_COLOUR}")

    return_to_main_menu_prompt()
```

- Clears terminal.
- Searches and selects a profile by the user entering a search field and ID, the same way as shown above.
- Then 2 conditions are checked, if either are met then an error message is shown respective to the condition met:
  - `is_user_active()` takes in the users enddate, this function checks if the enddate is not before today.
  - `check_user_logged_today()` takes in the users visit entrys, this fucntion checks if the user has logged in today already.
- If both conditions are not met, `get_todays_date()` function in sheets.py is used ti handle updating the apropriate profiles visits entrys to add todays entry.
- return to menu prompt

### Make a Payment

```python
def make_a_payment():
    clear_terminal()
    search_for_a_profile()
    Id = int(get_user_input_id())
    data = gsheet.get_history_data(Id)

    print(f"{WHITE}Now choose how many months to add (example: 3) >")
    print(f"                {YELLOW}1{WHITE} Month -> £{PAYMENT_AMOUNT_1MONTH}")
    print(f"                {YELLOW}3{WHITE} Month -> £{PAYMENT_AMOUNT_3MONTH}")
    print(f"                {YELLOW}6{WHITE} Month -> £{PAYMENT_AMOUNT_6MONTH}")
    print(f"                {YELLOW}9{WHITE} Month -> £{PAYMENT_AMOUNT_9MONTH}")
    print(f"                {YELLOW}12{WHITE} Month -> £{PAYMENT_AMOUNT_12MONTH}")

    months = int(get_user_input("Option",valid.validate_option,YELLOW,[1,3,6,9,12]))

    payment_amount = None

    if months == 1:
        payment_amount = PAYMENT_AMOUNT_1MONTH
    elif months == 3:
        payment_amount = PAYMENT_AMOUNT_3MONTH
    elif months == 6:
        payment_amount = PAYMENT_AMOUNT_6MONTH
    elif months == 9:
        payment_amount = PAYMENT_AMOUNT_9MONTH
    elif months == 12:
        payment_amount = PAYMENT_AMOUNT_12MONTH

    old_enddate = data[4]
    new_enddate = calculate_new_enddate(old_enddate,months)
    gsheet.add_payment(payment_amount,valid.get_todays_date(),new_enddate,Id,data[2])
    print(f"{GREEN} Payment Made")
    return_to_main_menu_prompt()
```

- Clears terminal.
- Searches and selects a profile by the user entering a search field and ID, the same way as shown above.
- User is presented with 5 different options, to select the package for the payment being made.
- using `get_user_input()` and also passing a list of options in, user will ener in a option which untill validated, will intilize a variable `payment_amount` and asign it to the respective global variable comtaing the payments price.
- A new enddate is calculated with a function `calculate_new_enddate()` which will take in the current enddate and months to be added, to then return a real life and valid date in the form DD/MM/YYYY.
- `add_payment()` function in sheets.py is used to handle adding the payment entry to the apropriate profile in historys sheet.
- return to menu prompt.

### Delete a Profile

```python
def delete_a_profile():
    clear_terminal()
    search_for_a_profile()
    Id = int(get_user_input_id())
    data = gsheet.get_all_profile_data()[Id]

    print_preview_profile(data)
    print_history_table(gsheet.get_history_data(Id))

    print(f"{WHITE}Are you sure you would like to delete this profile and its history data {RED}PERMANTLY{WHITE}, enter '{YELLOW}confirm'{WHITE} to delete this profile")
    confirmation = get_user_input("Confirmation",valid.validate_confirmation,YELLOW)
    gsheet.delete_row_at_id(Id)
    print(f"{GREEN}Profile and its history deleted")
    return_to_main_menu_prompt()
```

- Clears terminal.
- Searches and selects a profile by the user entering a search field and ID, the same way as shown above.
- Previews the profiles data from both sheets (profiles and history)in 2 respective tables.
- User must enter 'confirm' to console in any case to make sure they would like to delete this certain customers data from both sheets.
- Once conformed, `delete_row_at_id()` function in sheets.py is used to handle the removal of all that customers data, and also reasgining all customers ID numbers to make sure they are back in order after a customer deletion.
- return to main menu prompt.

## Technologies Used

- Python: All backend logic. Below are the libaries used and its justification:
  - gspread / google.oauth2.service_account / Credentials: All used to esatblish and use the API to/from Google Sheets.
  - os: To determine how to clear the terminal for different operating systems as they are slightly different to do.
  - re: Regex patterns in strings
  - datetime: Obtaining todays date.
- Git: Version control
- GitHub: Store repository online with change logs for other people to see.
- GitPod / VSCode: Envoronment in which this was built in.
- Heroku: Used to deploy the website online for other people to use.

## Testing

### CI Python Linter Validation (PEP8)

Link to the exact linter used can be found [here](https://pep8ci.herokuapp.com/#)
run.py

- ![python linter checks for run.oy](/README_assets/doc_17.png)
- Errors are from the ASCII 'GYM face' logo.
- Apart from this, no errors.

sheets.py

- ![python linter checks for run.oy](/README_assets/doc_18.png)
- No errors

validator.py

- ![python linter checks for run.oy](/README_assets/doc_19.png)
- No Errors

### Testing

| **Screen**           | **Feature**                   | **Expectation**                                                                                                                                           | **Result** |
| -------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **General**          | Terminal Setup                | Objects are created, establish API connection, attributes assigned to certain objects.                                                                    | **PASS**   |
|                      | Return to Menu Prompt         | User presses enter to return to menu, clearing the terminal, then displaying the main menu.                                                               | **PASS**   |
|                      | Searching for a Profile       | Searches for a profile based on input criteria and displays matching profiles.                                                                            | **PASS**   |
|                      | Selecting Profile by ID       | Validates ID input and retrieves the correct profile for editing.                                                                                         | **PASS**   |
| **Main Menu**        | Entering Menu Option          | Value entered has to be a numbered option and changes screen according to the option chosen; otherwise, it throws an error and displays an error message. | **PASS**   |
| **See All Data**     | Displaying Profiles           | Displays all profiles in an organized, color-coded table.                                                                                                 | **PASS**   |
| **Create A Profile** | Entering First Name           | Validates name (only letters, at least 2 characters), then stores the input.                                                                              | **PASS**   |
|                      | Entering Last Name            | Validates name (only letters, at least 2 characters), then stores the input.                                                                              | **PASS**   |
|                      | Entering Email Address        | Validates email format, then stores the input.                                                                                                            | **PASS**   |
|                      | Entering Phone Number         | Validates UK phone number format, then stores the input.                                                                                                  | **PASS**   |
|                      | Entering Date of Birth        | Validates date format (DD/MM/YYYY) and ensures it's a valid date before today.                                                                            | **PASS**   |
|                      | Finalizing Profile Creation   | Displays profile preview, adds profile to the database, and returns to the main menu.                                                                     | **PASS**   |
| **Edit A Profile**   | Editing Profile Fields        | Allows editing of first name, last name, email, phone number, or date of birth.                                                                           | **PASS**   |
|                      | Confirming and Saving Changes | Updates the profile in the database with new values and returns to the main menu.                                                                         | **PASS**   |
| **Log A Visit**      | Checking Subscription Status  | Verifies if the user has an active subscription and has not already logged today.                                                                         | **PASS**   |
|                      | Logging a Visit               | Adds today's date to the visit history if conditions are met.                                                                                             | **PASS**   |
| **Make a Payment**   | Choosing Subscription Package | Allows selection of subscription package, updates payment entries, and extends the subscription.                                                          | **PASS**   |
| **Delete A Profile** | Confirming Deletion           | Requires typing "confirm" to permanently delete the profile from the database.                                                                            | **PASS**   |

## Deployment

### Google Sheets Setup

1. **Sign in to Google**:

   - Log into your Google account.

2. **Create a Spreadsheet**:

   - Open [Google Sheets](https://sheets.google.com) and start a new spreadsheet.

3. **Enable Google Sheets API**:

   - Visit the [Google API Library](https://console.developers.google.com), create a new project, and enable the "Google Sheets API".

4. **Create Service Account**:

   - In the "Credentials" tab, create a new service account, provide necessary details, and generate a JSON key file. Keep this file secure.

5. **Share Spreadsheet**:
   - Share your Google Sheets file with the service account using the email found in the JSON file.

### GitHub Repository Setup

1. **Fork and Clone Repository**:

   - Fork the repository on GitHub and clone it locally using the URL provided.

2. **Set Up Local Environment**:

   - Ensure your `creds.json` file is added to `.gitignore` to avoid exposing credentials.

3. **Install Dependencies**:
   - Run `pip install -r requirements.txt` to install required libraries.

### Deployment to Heroku

1. **Prepare Dependencies**:

   - Run `pip3 freeze > requirements.txt` to set dependencies. Include any additional libraries manually.

2. **Create Heroku App**:

   - Create a new app on Heroku, add necessary config vars (`CREDS` and `PORT`), and set buildpacks for Python and Node.js.

3. **Deploy**:
   - Connect your GitHub repository to Heroku, and deploy the app by selecting the appropriate branch.

## Credits

- 'GYM face' ASCII logo made from the website [Patorjk](https://patorjk.com/software/taag/)
- Use of ANSI colour codes to display different coloured text to terminal was suggested and inspired by [Chat GPT](https://openai.com/index/chatgpt/)
- Regex pattern matching was inspired by program examples on [Stack Overflow](https://stackoverflow.com/)
- Program features was inspired by p-harting's [Console CRM](https://github.com/p-harting/console-crm)
- Google Sheets API settup and functionality, and feedback from my mentor Akshat Garg from [Code Institute](https://codeinstitute.net/)
