import csv
import xml.etree.ElementTree as ET
import os

# Set the source and destination folders
source_folder = '_data/researchers/xml_papers'
destination_folder = '_data/researchers/papers'

# Get a list of all XML files in the source folder
file_list = [file for file in os.listdir(source_folder) if file.endswith('.xml')]

# Loop through each XML file
for file_name in file_list:
    # Construct the full file paths
    source_path = os.path.join(source_folder, file_name)
    destination_path = os.path.join(destination_folder, file_name)

    # Parse the XML file
    tree = ET.parse(source_path)
    root = tree.getroot()

    # Define a function to extract the publication type
    def get_pub_type(element):
        if element.tag == 'article':
            return 'article'
        elif element.tag == 'inproceedings':
            return 'inproceedings'
        else:
            return None

    # Extract the necessary data
    rows = []

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
            row = [', '.join(author_names), title, journal, f"{volume}({year}): {pages}", doi, 'article']
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
            row = [', '.join(author_names), title, booktitle, f"{year}: {pages}", doi, 'inproceedings']
            rows.append(row)

    # Write data to CSV file
    csv_file_name = os.path.splitext(file_name)[0] + '.csv'
    csv_file_path = os.path.join(destination_folder, csv_file_name)
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Authors', 'Title', 'Journal/Booktitle', 'Volume/Pages', 'DOI', 'Type'])
        writer.writerows(rows)

    print(f"CSV file '{csv_file_name}' created successfully.")

print("All XML files processed.")

