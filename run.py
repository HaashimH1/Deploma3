# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from sheets import GoogleSheets


gsheet = GoogleSheets()

print(gsheet.get_data())