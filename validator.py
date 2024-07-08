import re    
from datetime import datetime


class Validator:

    def __init__(self,ERROR_COLOUR,RESET_COLOUR):
        self.ERROR_COLOUR = ERROR_COLOUR
        self.RESET_COLOUR = RESET_COLOUR
        

    def validate_name(self,name):

        if len(name) < 2:
            self.print_to_terminal("Name","be at least 2 characters")
            return False
        elif not name.isalpha():
            self.print_to_terminal("Name","be only letters")
            return False
        else:
            return True



    def validate_email(self,email):
        
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            return True
        else:
            self.print_to_terminal("Email Address","follow valid structure")
            return False



    def validate_phone(self,phone):

        if not re.match(r'^447\d{9}$', phone):
            self.print_to_terminal("Phone Number","be in the format of 447XXXXXXXXX, and 12 digits long")
            return False
        else:
            return 
            

    def validate_dob(self,dob):

        date_valid = self.validate_date(dob)

        if not date_valid==True:
            self.print_to_terminal("Date of Birth",date_valid)
            return False
        elif not self.is_date_before_today(dob):
            self.print_to_terminal("Date of Birth","be a date before today")
            return False
        else:
            return True





    def validate_date(self,date):
        
        if not re.match(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$', date):
            return "be in the right format of DD/MM/YYYY"
        elif not self.check_if_date_is_real(date):
            return "be a real date"
        else:
            return True


    def check_if_date_is_real(self,date):

        day, month, year = date.split('/')
        day = int(day)
        month = int(month)
        year = int(year)
    
        try:
            datetime(year, month, day)
            return True
        except ValueError:
            return False

    def is_date_before_today(self,date):

        day, month, year = date.split('/')
        day = int(day)
        month = int(month)
        year = int(year)

        input_date = datetime(year, month, day)
        today_date = datetime.today()

        if input_date < today_date:
            return True    # date given is before todays date
        else:
            return False   # date given is after todays date

        

    def print_to_terminal(self,field,error_message):
        print(f"{self.ERROR_COLOUR}Invalid {field}{self.RESET_COLOUR}: Must {error_message}")
            
            
