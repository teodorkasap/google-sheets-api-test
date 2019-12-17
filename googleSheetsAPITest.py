import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pandas as pd

scope = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("test-sheet-api").sheet1  # Open the spreadhseet


data = sheet.get_all_records()  # Get a list of all records
headers = data.pop(0)

pprint(data)

# client.copy("12v8cH4zsiqRDlLvawGGn2u6-mGNsv6uCtxGYuXnwNyI",
#             "test-sheet-api2",
#             copy_permissions=True)

# workbook = client.open("test-sheet-api2").sheet1  # Open the spreadhseet

df = pd.DataFrame(data,columns=headers)
print(df)
