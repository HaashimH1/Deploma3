import re    


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
            return True

    def validate_date(self,date):
        pass


                

    
    def print_to_terminal(self,field,error_message):
        print(f"{self.ERROR_COLOUR}Invalid {field}{self.RESET_COLOUR}: Must {error_message}")
            
            
