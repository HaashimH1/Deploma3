# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high



from sheets import GoogleSheets
from validator import Validator

# All global variables
gsheet = None
valid = None
# Colour codes for printing to terminal
BORDER_COLOUR = "\033[97m"    # white
ID_COLOUR = "\033[91m"        # red
FNAME_COLOUR = "\033[92m"     # green
LNAME_COLOUR = FNAME_COLOUR   # green
EMAIL_COLOUR = "\033[93m"     # orange
PHONE_COLOUR = "\033[95m"
DOB_COLOUR = "\033[94m"
MEMBER_COLOUR = "\033[92m"
ENDDATE_COLOUR = MEMBER_COLOUR
RESET_COLOUR = "\033[0m"
ERROR_COLOUR = ID_COLOUR

def main():

    print("setting up...")
    global gsheet
    global valid
    gsheet = GoogleSheets()
    valid = Validator(ERROR_COLOUR,RESET_COLOUR)

    print("getting all data")
    print_table(gsheet.get_all_data())
    add_new_profile()


def add_new_profile():
   
    firstname = get_user_input("First Name",valid.validate_name,FNAME_COLOUR)
    lastname = get_user_input("last Name",valid.validate_name,LNAME_COLOUR)  
    email = get_user_input("Email Address",valid.validate_email,EMAIL_COLOUR)
    phone = get_user_input("Phone Number",valid.validate_phone,PHONE_COLOUR)
    dob = get_user_input("Date of Birth",valid.validate_dob,DOB_COLOUR)
    member = get_user_input("Member (True or False)",valid.validate_member,MEMBER_COLOUR).upper()
    enddate = ""
    if(member == "TRUE"):   # only enters member end date if person is a member
        enddate = get_user_input("Member End Date",valid.validate_enddate,ENDDATE_COLOUR)
    Id = len(gsheet.get_all_data())

    new_row = [str(Id),firstname,lastname,email,str(phone),dob,member,enddate]
    print("adding this new row...")
    print_table([["ID","firstname","lastname","email","phone","dob","member","enddate"],new_row])
    gsheet.add_new_row(new_row)
    print("New Pofile succesfully added to database")
    



def get_user_input(field,validate_function,colour):
    while True:
        user_input = input(f"{BORDER_COLOUR}Please enter a {colour}{field}{RESET_COLOUR} >\n")
        if validate_function(user_input):
            return user_input



def print_table(data):

    # Calculate the maximum length for firstname, lastname, and email columns
    max_firstname_len = max(len(row[1]) for row in data)
    max_lastname_len = max(len(row[2]) for row in data)
    max_email_len = max(len(row[3]) for row in data)

    # Calculate the total length for the border dashes
    border_dashes_count = 49 + max_firstname_len + max_lastname_len + max_email_len 
    dashes = BORDER_COLOUR+("━" * border_dashes_count)+"\n"

    # Create the table with the top border
    table = dashes

    # Format each row and add it to the table
    for i, row in enumerate(data):
        table += f"{BORDER_COLOUR}│"
        table += f"{ID_COLOUR}{row[0].upper():>2}{BORDER_COLOUR}│"
        table += f"{FNAME_COLOUR}{row[1].upper():>{max_firstname_len}}{BORDER_COLOUR}│"
        table += f"{LNAME_COLOUR}{row[2].upper():<{max_lastname_len}}{BORDER_COLOUR}│"
        table += f"{EMAIL_COLOUR}{row[3].upper():>{max_email_len}}{BORDER_COLOUR}│"
        table += f"{PHONE_COLOUR}{row[4].upper():<12}{BORDER_COLOUR}│"
        table += f"{DOB_COLOUR}{row[5].upper():<10}{BORDER_COLOUR}│"
        table += f"{MEMBER_COLOUR}{row[6].upper():>6}{BORDER_COLOUR}│"
        table += f"{ENDDATE_COLOUR}{row[7].upper():<10}{BORDER_COLOUR}│"
        table += "\n"

        # adds border below header row
        if i == 0:
            table += dashes

    # Add the bottom border
    table += dashes
    print(table)
            


if __name__ == "__main__":
    main()





