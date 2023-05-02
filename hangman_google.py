import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_score')

def send_data(name, score, timestamp):
    values = [timestamp, name, score]

def append_data_to_sheet(values):
    worksheet = SHEET.get_worksheet(0)
    worksheet.append_row(values)

def get_all_data():
    worksheet = SHEET.get_worksheet(0)
    return worksheet.get_all_records()
