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


    def add_new_row(self,data:tuple):
        self.profiles.append_row(data)
        

    def delete_row_at_id(self,id:int):
        print(f"deleting row at id: {id}")
        self.profiles.delete_rows(id+1)    # id + 1 because 1st row is category headers
        self.reasign_ids()


    def reasign_ids(self):
         print("reassigning IDs...")
         for i in range(1, len(self.profiles.get_all_values())):
             self.profiles.update_cell(i + 1, 1, i)
        
        

        

        


