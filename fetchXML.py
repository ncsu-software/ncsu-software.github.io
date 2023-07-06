import csv
import xml.etree.ElementTree as ET
import os
import requests

# Read URL from CSV file
csv_file = "_data/researchers/researchersNew.csv"  # Update with your CSV file path
# Set the destination folder
destination_folder = '_data/researchers/'

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
            xml_data = response.text
            # Parse the XML data
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

header_columns=['email','Authors','Title','Journal','Volume','DOI','Type','Area','boast text','pdf','select']

if not os.path.isfile(csv_file_path):
    # Create the file and write the header columns
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header_columns)

# Append new rows to the existing CSV file
with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    for row in rows:
        writer.writerow(row)

print(f"CSV file '{csv_file_name}' updated successfully.")
