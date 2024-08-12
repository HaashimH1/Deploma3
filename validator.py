import re
from datetime import datetime


class Validator:

    def __init__(self, ERROR_COLOUR, RESET_COLOUR):
        """
        attributes holding colour codes for printing to terminal
        """
        self.ERROR_COLOUR = ERROR_COLOUR
        self.RESET_COLOUR = RESET_COLOUR

    def is_integer(self, number, field):
        """
        checks to see if number passed in is an integer

        param number: user input
        param field: ID in this case

        return: True if integer, false otherwise
        """
        try:
            int(number)
        except ValueError:
            self.print_to_terminal(field, "be a number")
            return False
        else:
            return True

    def validate_option(self, user_option, all_options, field):
        """
        validates option chosen from a range given as a list

        param user_option: user input
              all_options: list containing all valid options
              field: options in this case

        return: true if options is valid, false otherwise
        """
        try:
            if int(user_option) in all_options:
                return True
            else:
                self.print_to_terminal(field, f"be {all_options}")
                return False
        except ValueError:
            self.print_to_terminal(field, "be a number")
            return False

    def validate_name(self, name, field):
        """
        validates first and last name fields

        param name: user input
              field: name in this case

        return: true if valid name, false otherwise
        """
        if len(name) < 2:
            self.print_to_terminal(field, "be at least 2 characters")
            return False
        elif not name.isalpha():
            self.print_to_terminal(field, "be only letters")
            return False
        else:
            return True

    def validate_email(self, email, field):
        """
        validates email fields

        param email: user input
              field: email in this case

        return: true if valid email, false otherwise
        """
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
                    email):
            return True
        else:
            self.print_to_terminal(field, "follow valid structure")
            return False

    def validate_phone(self, phone, field):
        """
        validates phone number fields in uk format

        param phone: user input
              field: phone number in this case

        return: true if valid phone number, false otherwise
        """
        if not re.match(r'^447\d{9}$', phone):
            self.print_to_terminal(field, "be in the format of 447XXXXXXXXX")
            return False
        else:
            return True

    def validate_dob(self, dob, field):
        """
        validates date of birth fields

        param dob: user input
              field: date of birth in this case

        return: true if valid date of birth, false otherwise
        """
        # checks if dob given is a real date
        date_valid = self.validate_date(dob)

        if not date_valid:
            self.print_to_terminal(field, date_valid)
            return False
        elif not self.is_date_before_today(dob):
            self.print_to_terminal(field, "be a date before today")
            return False
        else:
            return True

    def validate_date(self, date):
        """
        checks if date given is a real date

        param date: date given

        return: true if valid date, error message otherwise
        """
        if not re.match(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$', date):
            return "be in the right format of DD/MM/YYYY"
        elif not self.check_if_date_is_real(date):
            return "be a real date"
        else:
            return True

    def validate_confirmation(self, confirm, field):
        """
        validates a confirmation field

        param confirm: user input
              field: confirmation in this case

        return: true if valid confirmation, false otherwise
        """
        if confirm.lower() == "confirm":
            return True
        else:
            self.print_to_terminal(field, "be 'confirm'")
            return False

    def check_if_date_is_real(self, date):
        """
        checks if date is a real date

        param date: date given

        return: true if real date, false otherwise
        """
        day, month, year = date.split('/')

        day = int(day)
        month = int(month)
        year = int(year)

        try:
            datetime(year, month, day)
            return True
        except ValueError:
            return False

    def is_date_before_today(self, date):
        """
        checks to see if a date given is before today or not

        param date: date given to check

        return: true if date if before today, false otherwise
        """
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

    def get_todays_date(self):
        """
        returns todays date back in DD/MM/YYYY format
        """
        today = datetime.today()
        uk_format_date = today.strftime("%d/%m/%Y")
        return uk_format_date

    def print_to_terminal(self, field, error_message):
        """
        printing to terminal with fields and error messages if
        data was not valid

        param field: field of the invalid data
              error_message: message to display to terminal of
                             what caused the error
        """
        print(f"{self.ERROR_COLOUR}Invalid {field}"
              f"{self.RESET_COLOUR}: Must {error_message}")
