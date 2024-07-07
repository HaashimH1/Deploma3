# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from sheets import GoogleSheets
from validator import Validator


# All global variables
valid = None
gsheet = None


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
    max_email_len = max(len(row[4]) for row in data)

    # Calculate the total length for the border dashes
    border_dashes_count = 60 + max_firstname_len + max_lastname_len + max_email_len 
    dashes = "━" * border_dashes_count

    # Create the table with the top border
    table = f"{dashes}\n"

    # Format each row and add it to the table
    for i, row in enumerate(data):
        table += "│"
        table += f"{row[0].upper():2}│"
        table += f"{row[1].upper():<{max_firstname_len}}│"
        table += f"{row[2].upper():<{max_lastname_len}}│"
        table += f"{row[3].upper():10}│"
        table += f"{row[4].upper():<{max_email_len}}│"
        table += f"{row[5].upper():12}│"
        table += f"{row[6].upper():10}│"
        table += f"{row[7].upper():6}│"
        table += f"{row[8].upper():10}│"
        table += "\n"

        # adds border below header row
        if i == 0:
            table += f"{dashes}\n"

    # Add the bottom border
    table += dashes

    

    # Print the table
    print(table)
            



    


if __name__ == "__main__":
    main()





