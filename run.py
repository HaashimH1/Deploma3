# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from sheets import GoogleSheets
from validator import Validator


# All global variables
valid = None
gsheet = None

# Colour codes for printing to terminal
BORDER_COLOUR = "\033[97m"
ID_COLOUR = "\033[91m"
FNAME_COLOUR = "\033[92m"
LNAME_COLOUR = FNAME_COLOUR
EMAIL_COLOUR = "\033[93m"
PHONE_COLOUR = "\033[95m"
DOB_COLOUR = "\033[94m"
MEMBER_COLOUR = "\033[92m"
ENDDATE_COLOUR = MEMBER_COLOUR

def main():

    print("setting up...")

    global valid
    global gsheet

# objects to access methods of repective classes
    valid = Validator()
    gsheet = GoogleSheets()

    print_table(gsheet.get_all_data())



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
        table += f"{ID_COLOUR}{row[0].upper():2}{BORDER_COLOUR}│"
        table += f"{FNAME_COLOUR}{row[1].upper():<{max_firstname_len}}{BORDER_COLOUR}│"
        table += f"{LNAME_COLOUR}{row[2].upper():<{max_lastname_len}}{BORDER_COLOUR}│"
        table += f"{EMAIL_COLOUR}{row[3].upper():<{max_email_len}}{BORDER_COLOUR}│"
        table += f"{PHONE_COLOUR}{row[4].upper():12}{BORDER_COLOUR}│"
        table += f"{DOB_COLOUR}{row[5].upper():10}{BORDER_COLOUR}│"
        table += f"{MEMBER_COLOUR}{row[6].upper():6}{BORDER_COLOUR}│"
        table += f"{ENDDATE_COLOUR}{row[7].upper():10}{BORDER_COLOUR}│"
        table += "\n"

        # adds border below header row
        if i == 0:
            table += dashes

    # Add the bottom border
    table += dashes
    print(table)
            


if __name__ == "__main__":
    main()





