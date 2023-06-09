import csv
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('_data\john_doe.xml')
root = tree.getroot()

# Extract the necessary data
rows = []

r_elements = root.findall('r')
for r in r_elements:
    article = r.find('article')
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
        row = [', '.join(author_names), title, journal, f"{volume}({year}): {pages}",doi]
        rows.append(row)

# Write data to CSV file
with open('_data\john_doe.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Authors', 'Title', 'Journal', 'Volume','DOI'])
    writer.writerows(rows)

print("CSV file created successfully.")
