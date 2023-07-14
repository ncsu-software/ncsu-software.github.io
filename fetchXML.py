import csv
import xml.etree.ElementTree as ET
import os
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import traceback

# Read URL from CSV file
csv_file = "_data/researchers/sheets/ResearchersResponses.csv"  # Update with your CSV file path
# Set the destination folder
destination_folder = '_data/researchers/sheets'

existing_rows = []  # List to store existing rows

# Read existing rows from CSV file
csv_file_name = 'researchPapers.csv'
csv_file_path = os.path.join(destination_folder, csv_file_name)

if os.path.exists(csv_file_path):
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        existing_rows = list(reader)

rows = []

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for researcher_row in reader:
        url = researcher_row['dblp']
        email = researcher_row['EmailAddress']
        # Make GET API request
        response = requests.get(url)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            try:
                xml_data = response.text
                # Parse the XML data
                print("\n Researcher: ", email)
                root = ET.fromstring(xml_data)

                # Extract the necessary data

                r_elements = root.findall('r')
                for r in r_elements:
                    article = r.find('article')
                    inproceedings = r.find('inproceedings')

                    if article is not None:
                        author_names = []
                        for author in article.findall('author'):
                            author_names.append(author.text)

                        title = article.find('title').text
                        journal = article.find('journal').text
                        volume = article.find('volume').text
                        pages_element = article.find('pages')
                        pages = pages_element.text if pages_element is not None else ""
                        doi = article.find('ee')
                        doi = doi.text if doi is not None else ""
                        year = article.find('year').text
                        row = [researcher_row['EmailAddress'],', '.join(author_names), title, journal, f"{volume}({year}): {pages}", doi, 'article',"","","",""]

                        # Check if row already exists based on matching columns
                        if any(row[:7] == existing_row[:7] for existing_row in existing_rows):
                            continue  # Skip adding the row if it already exists

                        rows.append(row)

                    if inproceedings is not None:
                        author_names = []
                        for author in inproceedings.findall('author'):
                            author_names.append(author.text)

                        title = inproceedings.find('title').text
                        booktitle = inproceedings.find('booktitle').text
                        pages_element = inproceedings.find('pages')
                        pages = pages_element.text if pages_element is not None else ""
                        doi = inproceedings.find('ee')
                        doi = doi.text if doi is not None else ""
                        year = inproceedings.find('year').text
                        row = [researcher_row['EmailAddress'],', '.join(author_names), title, booktitle, f"{year}: {pages}", doi, 'inproceedings',"","","",""]

                        # Check if row already exists based on matching columns
                        if any(row[:7] == existing_row[:7] for existing_row in existing_rows):
                            continue

                        rows.append(row)
            except Exception as e:
                print("\n\n\n\n\n$$$$$$$$$$$$$$$$$$$   ERROR: ",e)
                

header_columns=['EmailAddress','Authors','Title','Journal','Volume','DOI','Type','Area','boast text','pdf','select']

if not os.path.isfile(csv_file_path):
    # Create the file and write the header columns
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header_columns)

# Append new rows to the existing CSV file
with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Check if the file is empty
    if csvfile.tell() == 0:
        writer.writerow(header_columns)  # Write the header row if the file is empty
        
    for row in rows:
        writer.writerow(row)  # Write the data rows


print(f"CSV file '{csv_file_name}' updated successfully.")


researchPapers={
    'gid': '739778209',
    'sheet_id': '1nQWPQR_ZeW5YDSQYa0uUTMx0rkRNMYk_BW1PR6OKyXI',
    'sheet_name': 'researchPapers',
    'form_url':''
}


researchPapers_tim={
    'gid': '800333832',
    'sheet_id': '1UTVX6_wsak20TgdDfPv198mJ50MGH9HgtMDDWRGOtks',
    'sheet_name': 'researchPapers',
    'form_url':''
}

# Set the path to your Google Sheets credentials JSON file
credentials_path = 'credentials.json'

# Define the scope of the Google Sheets API
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Create credentials using the JSON file and the defined scope
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scopes)

# Authorize the credentials
client = gspread.authorize(credentials)

# Function to upload a CSV file to Google Sheets
def upload_csv_to_google_sheets(file_path, sheet_id):
    # Open the Google Sheet by its ID
    sheet = client.open_by_key(sheet_id)

    # Get the specified sheet by name
    worksheet = sheet.worksheet('Form Responses 1')

    # Read the CSV file
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        data = list(csv_data)

    # Clear the existing content in the worksheet
    worksheet.clear()

    # Upload the CSV data to Google Sheets
    worksheet.append_rows(data)

    print(f"CSV file '{file_path}' uploaded to Google Sheets.")
    

upload_csv_to_google_sheets(csv_file_path,researchPapers_tim['sheet_id'])
