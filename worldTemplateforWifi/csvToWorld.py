import pandas as pd
from docx import Document
from docx.shared import Pt

# Load the CSV file with user credentials
user_data = pd.read_csv(r'worldTemplateforWifi\userCredentials.csv', header=None)

# Define column names based on the file's structure
user_data.columns = ['username', 'password', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9']

# Open the Word template document
template_path = r'worldTemplateforWifi\template.docx'

# Function to make text bold in a paragraph
def make_bold(paragraph, search_text, replacement_text):
    # Search for the placeholder text in the paragraph
    if search_text in paragraph.text:
        # Clear the paragraph and add bolded text
        for run in paragraph.runs:
            # If the search text is found, split and replace with bold
            if search_text in run.text:
                run.text = run.text.replace(search_text, replacement_text)
                run.bold = True
            else:
                # Keep the rest of the text as normal
                run.bold = False

# Process each user in the CSV
for index, row in user_data.iterrows():
    username = row['username']
    password = row['password']

    # Load the template Word document
    doc = Document(template_path)

    # Replace placeholders with actual data and make them bold
    for paragraph in doc.paragraphs:
        make_bold(paragraph, "{{USERNAME}}", username)
        make_bold(paragraph, "{{PASSWORD}}", password)

    # Save the document with a unique filename for each user
    output_path = f'worldTemplateforWifi\worlds\{username}_wifi.docx'
    doc.save(output_path)
    print(f'Saved: {output_path}')
