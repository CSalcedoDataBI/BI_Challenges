# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7172803509036290048-2cU-?utm_source=share&utm_medium=member_desktop
import pandas as pd

# Define the path to the Excel file
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_409 - Table_Regular.xlsx"

# Read the Excel file into a pandas DataFrame, selecting only columns A to E and limiting to the first 11 rows
df = pd.read_excel(file_path, usecols="A:E", nrows=11)

# Split the string in 'Items' column by commas, converting each item into a list of items
df['Items'] = df['Items'].str.split(',')

# Explode the 'Items' column to create a new row for each item in the list while keeping the other column values intact
df_exploded = df.explode('Items')

# Strip leading and trailing whitespace from the 'Items' column to clean up the data
df_exploded['Items'] = df_exploded['Items'].str.strip()

# Fill NaN values down the DataFrame in the 'Categories' and 'Note' columns to handle missing data
df_filled = df_exploded.fillna(method='ffill')

# Reset the index of the DataFrame to ensure it is sequential after the explode and fill operations
df_filled.reset_index(drop=True, inplace=True)

# Display the first 200 rows of the final DataFrame to review the results
df_filled.head(200)
