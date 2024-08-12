import gspread
from google.oauth2.service_account import Credentials

# Global var for custom data to access google sheet as may be updated
SPREADSHEET_NAME = "Deploma3"
SHEET_NAME1 = "Profile"
SHEET_NAME2 = "History"
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


class GoogleSheets:

    # setup API to google sheet
    def __init__(self):
        """
        Setting up the attributs for the GoogleSheets objects
        for using the API easily

        """
        self.CREDS = Credentials.from_service_account_file("creds.json")
        self.SCOPED_CREDS = self.CREDS.with_scopes(SCOPE)
        self.GSPREAD_CLIENT = gspread.authorize(self.SCOPED_CREDS)
        self.SHEET = self.GSPREAD_CLIENT.open(SPREADSHEET_NAME)
        self.profiles = self.SHEET.worksheet(SHEET_NAME1)
        self.history = self.SHEET.worksheet(SHEET_NAME2)

    # retrieves the data from the sheet
    def get_all_profile_data(self):
        """
        Gets all profile sheets data

        return: data as a list of lists

        """
        data = self.profiles.get_all_values()
        return data

    def get_history_data(self, id):
        """
        Gets all history data for a given profile

        param id: profiles ID

        return: list of history data
        """
        data = self.history.get_all_values()
        return data[id]

    def get_enddates(self):
        """
        Gets all enddates from history sheet

        return: list of enddates

        """
        data = self.history.col_values(5)
        return data

    def get_IDs(self):
        """
        Gets all ID's in profiles sheet

        return: list of ID's

        """
        data = self.profiles.col_values(1)
        return data

    def add_new_profile(self, data, Id, date):
        """
        Adds new row to both sheets for a newly created profile

        param data: list of fields for new profile
              Id: ID of new profile
              date: date of profile creation

        """
        self.profiles.append_row(data)
        self.add_new_profiles_history_data(Id, date)

    def add_new_profiles_history_data(self, Id, date):
        """
        Sets the new profiles history data

        param Id: ID of profile
              date: date of profile creation
        """
        data = [Id, date, "", "", date]
        self.history.append_row(data)

    def delete_row_at_id(self, id: int):
        """
        Deletes a profile on both sheets

        param id: ID of profile being deleted
        """
        self.profiles.delete_rows(id+1)  # id+1 because 1st row is field header
        self.history.delete_rows(id+1)
        self.reasign_ids()

    def reasign_ids(self):
        """
        After profile deletion, ID's are reasigned back in order

        """
        for i in range(1, len(self.profiles.get_all_values())):
            self.profiles.update_cell(i + 1, 1, i)
            self.history.update_cell(i + 1, 1, i)

    def add_visit(self, date, Id, visits_data):
        """
        Adds the visit to the history sheet for the profile

        param date: date of visit logged
              Id: profiles ID being updated
              visits_data: the data of all visits from this profile prior
                           to this visit being logged

        """
        visits_data += f"{date}|"
        self.history.update_cell(Id + 1, 4, visits_data)

    def add_payment(self, payment_amount, today_date,
                    enddate, Id, payments_data):
        """
        Adds the payment to the history sheet for the given profile

        param payment_amount: amount of payment
              today_date: todays date
              enddate: enddate for active subscription(s)
              Id: profiles ID being updated
              payments_data: the data of all payments from this profile prior
                             to this payment being logged
        """
        payments_data += f"{payment_amount},{today_date}|"
        self.history.update_cell(Id + 1, 3, payments_data)
        self.history.update_cell(Id + 1, 5, enddate)

    def update_profile(self, data):
        """
        Update a profile with new data

        param data: list of all fields for a profile

        """
        index = int(data[0]) + 1
        self.profiles.update(f"A{index}", [data])
