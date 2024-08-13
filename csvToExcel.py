import pandas as pd

# Load the CSV file
df = pd.read_csv('ISO 9001 Ölçme Anket.csv')

# Save the DataFrame to an Excel file
df.to_excel('data.xlsx', index=False)
