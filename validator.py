    
class Validator:

    def __init__(self,ERROR_COLOUR,RESET_COLOUR):
        self.ERROR_COLOUR = ERROR_COLOUR
        self.RESET_COLOUR = RESET_COLOUR
        

    def validate_name(self,name):
        try:
            if len(name) < 2:
                raise ValueError(f"Name must be at least 2 characters")
            if not name.isalpha():
                raise ValueError(f"Name must be only Letters")
            return True
        except ValueError as e:
            self.print_to_terminal("Name",e)
            return False

    
    def print_to_terminal(self,field,e):
        print(f"{self.ERROR_COLOUR}Invalid {field}{self.RESET_COLOUR}: {e}, Please Input Correctly")
            
            
