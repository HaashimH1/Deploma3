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
- ANSI colour codes for displaying different coloured texts to terminal to show differentiation between fields and focus and certain aspects.
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
Firstly, the terminal is cleared using this function below:

```python
def clear_terminal():
    # Check the OS and send the appropriate command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and Mac
        os.system('clear')
```
Then after displaying the menu option to user, a function `get_user_input()` is always used to obtain the input of ther user and make sure it is validated, below is the function:
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
    - If the user types 'menu' (case-insensitive), the function calls `main_menu()` to navigate back to the main menu.

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
- `print_to_terminal()` is a functions that is used to display the error message if a input is invalid for all fields, which will have arguements of the field being validated (exg: email) and the error message itself (be in the email format)

Below is that function:
```python
def print_to_terminal(self,field,error_message):
        print(f"{self.ERROR_COLOUR}Invalid {field}{self.RESET_COLOUR}: Must {error_message}")
```

- Then after the input is valid, a certain function is called and is determined by the option input.
Below is the whole `main_menu()` function:
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

### See All Data




