# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from sheets import GoogleSheets
from validator import Validator
import os

# All global variables
gsheet = None
valid = None
# Colour codes for printing to terminal

BLACK = "\033[30m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
WHITE = "\033[97m"
RESET_COLOUR = "\033[0m"

BORDER_COLOUR = WHITE
ID_COLOUR = RED
FNAME_COLOUR = GREEN
LNAME_COLOUR = GREEN
EMAIL_COLOUR = YELLOW
PHONE_COLOUR = PURPLE
DOB_COLOUR = BLUE

PAYMENT_AMOUNT_1MONTH = 29.99
PAYMENT_AMOUNT_3MONTH = 79.99
PAYMENT_AMOUNT_6MONTH = 149.99
PAYMENT_AMOUNT_9MONTH = 219.99
PAYMENT_AMOUNT_12MONTH = 249.99


def main():
    print(f"{GREEN}    Setting up...")
    global gsheet
    global valid
    gsheet = GoogleSheets()
    valid = Validator(RED,RESET_COLOUR)

    main_menu()

    
def main_menu():
   
    clear_terminal()
    print(f"\n\n          {YELLOW}Main Menu\n      {GREEN}Choose an Option:\n")
    print(f"     {BLUE}1 {WHITE}--> See all Data\n")
    print(f"     {BLUE}2 {WHITE}--> Create a Profile\n")
    print(f"     {BLUE}3 {WHITE}--> Edit a Profile\n")
    print(f"     {BLUE}4 {WHITE}--> Log a Visit\n")
    print(f"     {BLUE}5 {WHITE}--> Make a Payment\n")
    
    option = get_user_input("Option",valid.validate_option,BLUE,[1,2,3,4,5])
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

def see_all_data():
   
    clear_terminal()
    print(f"\n\n                   {GREEN}Getting all Profiles....\n")
    print_profile_table(gsheet.get_all_profile_data())
    print(f"{WHITE}To show the history of a customer:\n")
    Id = get_user_input_id()
    print(f"{GREEN}           Getting {ID_COLOUR}{Id}{GREEN}'s history data....")
    print_history_table(gsheet.get_history_data(int(Id)))
    return_to_main_menu_prompt()


    
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

def make_a_payment():
    
    clear_terminal()
    search_for_a_profile()
    Id = int(get_user_input_id())
    data = gsheet.get_history_data(Id)

 

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


def calculate_new_enddate(old_enddate,months):

    if valid.is_date_before_today(old_enddate):
        return add_months_onto_date(valid.get_todays_date(),months)   
    else:
        return add_months_onto_date(old_enddate,months)    # adds months onto enddate given to stack subscription periods
   

def add_months_onto_date(date,months_to_add):

    day,month,year = date.split("/")

    day = int(day)
    month = int(month)
    year = int(year)

    month += months_to_add

    if month > 12:
        month -= 12
        year += 1

    days_to_add = 0
    while not valid.check_if_date_is_real(f"{day}/{month}/{year}"):
        days_to_add += 1
        day -= 1 
    
    if days_to_add > 0:
        day = days_to_add
        month += 1

    if month > 12:
        month -= 12
        year += 1

    if day < 10:
        day = f"0{day}"
    if month < 10:
        month = f"0{month}"
    
    return f"{day}/{month}/{year}"

def search_for_a_profile():

    search_field = input(f"{WHITE}Enter a {BLUE}search field{WHITE} >\n")
    print(f"{GREEN} Searching for '{BLUE}{search_field}{GREEN}' ....")

    matching_profiles = get_profiles_by_search(str(search_field))
    print_profile_table(matching_profiles)

        
    
def check_user_logged_today(all_visits):

    each_visit = all_visits.split("|")
    for date in each_visit:
        if valid.get_todays_date() == date:
            return True
    return False


    


def get_profiles_by_search(search_field):

    all_profiles = gsheet.get_all_profile_data()
    matching_profiles = [all_profiles[0]] # asigns the headers

    for row in all_profiles[1:]:
        for item in row:
            if search_field in item:
                matching_profiles.append(row)
                break  # no need to search through this row if search criteria is found

    return matching_profiles




def get_user_input_id():
    while True:
        Id = get_user_input("ID",valid.is_integer,ID_COLOUR)
        if does_id_exist(Id):
            return Id
        else:
            print(f"{WHITE}The ID: {ID_COLOUR}{Id}{WHITE} does not exist")




def does_id_exist(input_Id):
    IDs = gsheet.get_IDs()
    for ID in IDs[1:]:
        if ID == input_Id:
            return True
    return False


def return_to_main_menu_prompt():
    input(f"{WHITE}Press {BLUE}ENTER{WHITE} to return to Main Menu{BLACK}\n")
    main_menu()


def get_user_input(field,validate_function,colour,options = []): # for menu options a list is passed in, if not options type validation then paramter is a empty list
    while True:                                                                                                                  
        user_input = input(f"{WHITE}Please enter a {colour}{field}{WHITE}, or type '{BLUE}menu{WHITE}' to go back to main menu >{RESET_COLOUR} \n")
        if user_input.lower() == "menu":
            main_menu()
        else:
            if options: 
                if validate_function(user_input,options,field):
                    return user_input
            else:
                if validate_function(user_input,field):
                    return user_input

        


def is_user_active(date):
    
    if valid.is_date_before_today(date):
        return False
    else:
        return True




def print_history_table(data):
    
    dashes = BORDER_COLOUR + ("━"*55)+"\n"
    table = dashes

    table += "│"
    table += f"{ID_COLOUR}ID{BORDER_COLOUR}│"
    table += f"{GREEN}SIGNUPDATE{BORDER_COLOUR}│"
    table += f"{YELLOW}    PAYMENTS     {BORDER_COLOUR}│"
    table += f"{PURPLE}  VISITS  {BORDER_COLOUR}│"
    table += f"{BLUE}  ENDATE  {BORDER_COLOUR}│"
    table += "\n"
    table += dashes

    payments = data[2].split("|")
    visits = data[3].split("|")

    number_of_rows = max(len(payments),len(visits)) - 1
    
    space = " "

    for i in range (number_of_rows):
        table += "│"
        
        if i == 0:
            table += f"{ID_COLOUR}{data[0]:>2}{BORDER_COLOUR}│"
            table += f"{GREEN}{data[1]}{BORDER_COLOUR}│"
            table += f"{YELLOW}{payments[0]:>17}{BORDER_COLOUR}│"
            table += f"{PURPLE}{visits[0]:10}{BORDER_COLOUR}│"
            table += f"{BLUE}{data[4]}{BORDER_COLOUR}│"
            table += "\n"
        else:
            table += space*2 + "│"
            table += space*10 + "│"
            try:
                table += f"{YELLOW}{payments[i]:>17}{BORDER_COLOUR}│"
            except:
                table += space*17 + "│"  # no payments for this row
            try:
                table += f"{PURPLE}{visits[i]:10}{BORDER_COLOUR}│"
            except:
                table += space*10 + "│"  # no visits for this row
            table += space*10 + "│"
            table += "\n"

    table += dashes

    print(table)
    




def print_profile_table(data):

    # Calculate the maximum length for firstname, lastname, and email columns
    max_firstname_len = max(len(row[1]) for row in data)
    max_lastname_len = max(len(row[2]) for row in data)
    max_email_len = max(len(row[3]) for row in data)

    # Calculate the total length for the border dashes
    border_dashes_count = 38 + max_firstname_len + max_lastname_len + max_email_len 
    dashes = BORDER_COLOUR+("━" * border_dashes_count)+"\n"

    # Create the table with the top border
    table = dashes

    # retrieves all enddates from history table instead of doing 
    enddates = get_enddates(data)

    # Format each row and add it to the table
    for i, row in enumerate(data):
        table += f"{BORDER_COLOUR}│"
        table += f"{ID_COLOUR}{row[0].upper():>2}{BORDER_COLOUR}│"
        table += f"{FNAME_COLOUR}{row[1].upper():>{max_firstname_len}}{BORDER_COLOUR}│"
        table += f"{LNAME_COLOUR}{row[2].upper():<{max_lastname_len}}{BORDER_COLOUR}│"
        table += f"{EMAIL_COLOUR}{row[3].upper():>{max_email_len}}{BORDER_COLOUR}│"
        table += f"{PHONE_COLOUR}{row[4].upper():<12}{BORDER_COLOUR}│"
        table += f"{DOB_COLOUR}{row[5].upper():<10}{BORDER_COLOUR}│"
        if i==0:
            table += f"{ID_COLOUR}ACTIVE{BORDER_COLOUR}│"
        else:
            table += f"{ID_COLOUR}{is_user_active(enddates[i]):<6}{BORDER_COLOUR}│"
        table += "\n"

        # adds border below header row
        if i == 0:
            table += dashes

    # Add the bottom border
    table += dashes
    print(table)
            
def get_enddates(data):
    
    all_enddates = gsheet.get_enddates()
    enddates = [all_enddates[0]]  # adds the headers

    for profile in data[1:]:
        enddates.append(all_enddates[int(profile[0])])

    return enddates



def print_preview_profile(data):

    dashes = BORDER_COLOUR + "━"*(30 + len(data[1]) + len(data[2]) + len(data[3]) ) + "\n"
    table = dashes
    
    table += "│"
    table += f"{ID_COLOUR}{data[0]}{BORDER_COLOUR}│"
    table += f"{FNAME_COLOUR}{data[1].upper()}{BORDER_COLOUR}│"
    table += f"{LNAME_COLOUR}{data[2].upper()}{BORDER_COLOUR}│"
    table += f"{EMAIL_COLOUR}{data[3].upper()}{BORDER_COLOUR}│"
    table += f"{PHONE_COLOUR}{data[4]}{BORDER_COLOUR}│"
    table += f"{DOB_COLOUR}{data[5]}{BORDER_COLOUR}│\n"
    table += dashes

    print(f"\n{table}")


def clear_terminal():
    """
    Clears the terminal screen.
    """
    # Check the OS and send the appropriate command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and Mac
        os.system('clear')



if __name__ == "__main__":
    main()





