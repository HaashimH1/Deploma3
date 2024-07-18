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
        self.CREDS = Credentials.from_service_account_file("creds.json")
        self.SCOPED_CREDS = self.CREDS.with_scopes(SCOPE)
        self.GSPREAD_CLIENT = gspread.authorize(self.SCOPED_CREDS)
        self.SHEET = self.GSPREAD_CLIENT.open(SPREADSHEET_NAME)
        self.profiles = self.SHEET.worksheet(SHEET_NAME1)
        self.history = self.SHEET.worksheet(SHEET_NAME2)


    
    # retrieves the data from the sheet
    def get_all_profile_data(self):
        data = self.profiles.get_all_values()
        return data
        
    def get_history_data(self,id):
        data = self.history.get_all_values()
        return data[id]
    
    def get_enddates(self):
        data = self.history.col_values(5)
        return data
        
    def get_IDs(self):
        data = self.profiles.col_values(1)
        return data


    def add_new_profile(self,data:tuple,Id,date):
        self.profiles.append_row(data)
        self.add_new_profiles_history_data(Id,date)

    def add_new_profiles_history_data(self,Id,date):
        data = [Id,date,"","",date]
        self.history.append_row(data)
        

    def delete_row_at_id(self,id:int):
        self.profiles.delete_rows(id+1)    # id + 1 because 1st row is category headers
        self.history.delete_rows(id+1) 
        self.reasign_ids()


    def reasign_ids(self):
         for i in range(1, len(self.profiles.get_all_values())):
             self.profiles.update_cell(i + 1, 1, i)
             self.history.update_cell(i + 1, 1, i)

    def add_visit(self,date,Id,visits_data):
        visits_data += f"{date}|"
        self.history.update_cell(Id + 1,4,visits_data)  # id + 1 because 1st row is category headers

    
    def add_payment(self,payment_amount,today_date,enddate,Id,payments_data):
        payments_data += f"{payment_amount},{today_date}|"
        self.history.update_cell(Id + 1,3,payments_data)
        self.history.update_cell(Id + 1,5,enddate)


    def update_profile(self,data):
        index = int(data[0]) + 1
        self.profiles.update(f"A{index}",[data])
        



        
        

        

        


