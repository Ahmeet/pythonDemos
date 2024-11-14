import pandas as pd
import random
import re

# Load the CSV file with real names
input_file = r'worldTemplateforWifi\realNames.csv'
user_data = pd.read_csv(input_file)

# Function to generate a username based on full name
def generate_username(full_name):
    # Convert the full name to lowercase and remove special characters
    parts = re.split(r'\s+', full_name.strip().lower())
    # Use first name and last name if available
    if len(parts) > 1:
        return f"{parts[0]}.{parts[-1]}"
    else:
        return parts[0]

# Function to generate a password in the format 'Gentek.xxxx'
def generate_password():
    return f"Gentek.{random.randint(1000, 9999)}"

# Create a list to store rows in the specified format
output_data = []
for _, row in user_data.iterrows():
    full_name = row['full_name']
    username = generate_username(full_name)
    password = generate_password()
    
    # Append the row in the required format
    output_data.append([
        username,           # Username in the first column
        password,           # Password in the second column
        "", "",             # Two empty columns
        full_name,          # Full name in the sixth column
        "", "0", "0", "0"   # Empty column and three zeros
    ])

# Convert the list of rows to a DataFrame
df = pd.DataFrame(output_data)

# Save the DataFrame to a CSV file without headers and index
output_file = r'worldTemplateforWifi\userCredentials.csv'
df.to_csv(output_file, index=False, header=False)
print(f"CSV file '{output_file}' has been created successfully.")
