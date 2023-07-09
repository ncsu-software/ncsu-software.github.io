import os
import gspread
import csv
from oauth2client.service_account import ServiceAccountCredentials

# Set the path where the local copies of the Google Sheets will be stored
local_copy_directory = '_data/researchers/sheets/'

# Define the Google Sheet IDs and corresponding sheet names
sheet_data = [
    {
        'gid': '1472042545',
        'sheet_id': '15q4HlhUb1TGyfPMMf-DwDgu8K5Y7eZLrRyBxBr7sKG8',
        'sheet_name': 'LabsResponses',
        'form_url':"https://forms.gle/wWqiUWXdP4KmX3pk8"
    },
    {
        'gid': '894675277',
        'sheet_id': '15X_IeQkdD7axoOTwbWClD7AFiOi5gKzxMoMES9aqU3k',
        'sheet_name': 'ResearchersResponses',
        'form_url': "https://forms.gle/72LCSdHEs63TW8HX7"
    },
    {
        'gid': '1225990390',
        'sheet_id': '1nUHjaEbW9LpEfjIG1Hmagz-p7geEdlBfvDiePphx2UA',
        'sheet_name': 'NewsResponses',
        'form_url':'https://forms.gle/Mcwho2X5SUBjpViP6'
    },
    {
        'gid': '1105421572',
        'sheet_id': '13rdPzgLBAL6iKzFZZ2ZJJbzXRg3YWb0WbmLMfvidbvc',
        'sheet_name': 'MantraResponses',
        'form_url':'https://forms.gle/L5Si1r8uYWhtBa4i8'
    },
    {
        'gid': '1331663599',
        'sheet_id': '1-AdrDmtW0yiJNMbklxm95bXUg2Nlj9fSWKSA-QaMfUA',
        'sheet_name': 'GrantsResponses',
        'form_url':'https://forms.gle/gyRANV7n4viQTVCP8'
    },
    {
        'gid': '1418776165',
        'sheet_id': '1g7zXmSe09GL6YKwv11KnUCg548hUYPw76N_9176SuZg',
        'sheet_name': 'EmploymentOpportunityResponses',
        'form_url':'https://forms.gle/Mr2WEri7dKnR49947'
    },
    {
        'gid': '469150075',
        'sheet_id': '1eKQwHTLvhTP0jx01X8n3CIN7FGpdbMP93QqBEjuoSKc',
        'sheet_name': 'CurrentStudentsResponses',
        'form_url':'https://forms.gle/BqtMafJgW1c6NYXV7'
    },
    {
        'gid': '739778209',
        'sheet_id': '1nQWPQR_ZeW5YDSQYa0uUTMx0rkRNMYk_BW1PR6OKyXI',
        'sheet_name': 'researchPapers',
        'form_url':''
    }
]

researchPapers={
    'gid': '739778209',
    'sheet_id': '1nQWPQR_ZeW5YDSQYa0uUTMx0rkRNMYk_BW1PR6OKyXI',
    'sheet_name': 'researchPapers',
    'form_url':''
}


# Function to upload a CSV file to Google Sheets
def upload_csv_to_google_sheets(file_path, sheet_id):
    # Open the Google Sheet by its ID
    sheet = client.open_by_key(sheet_id)

    # Get the specified sheet by name
    worksheet = sheet.worksheet('Sheet1')

    # Read the CSV file
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        data = list(csv_data)

    # Clear the existing content in the worksheet
    worksheet.clear()

    # Upload the CSV data to Google Sheets
    worksheet.import_csv(data)

    print(f"CSV file '{file_path}' uploaded to Google Sheets.")
    
# upload_csv_to_google_sheets()

# Set the path to your Google Sheets credentials JSON file
credentials_path = 'se-website-391805-69c37c84110c.json'

# Define the scope of the Google Sheets API
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Create credentials using the JSON file and the defined scope
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scopes)

# Authorize the credentials
client = gspread.authorize(credentials)

# Iterate over each Google Sheet in the sheet_data list
for data in sheet_data:
    # Open the Google Sheet by its ID
    sheet = client.open_by_key(data['sheet_id'])

    # Get the specified sheet by name
    worksheet = sheet.worksheet('Form Responses 1')

    # Get all values from the worksheet
    values = worksheet.get_all_values()

    # Change the column header from "Email Address" to "EmailAddress"
    for i, header in enumerate(values[0]):
        if header == "Email Address":
            values[0][i] = "EmailAddress"

    # Set the local copy path
    local_copy_path = os.path.join(local_copy_directory, f"{data['sheet_name']}.csv")

    # Save the values as CSV
    with open(local_copy_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(values)

    print(f"Google Sheet {data['sheet_name']} downloaded successfully as CSV.")

print("All Google Sheets downloaded successfully!")


