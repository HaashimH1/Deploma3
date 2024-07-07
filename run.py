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

    print(gsheet.get_all_data())
    gsheet.delete_row_at_id(3)
    


if __name__ == "__main__":
    main()





