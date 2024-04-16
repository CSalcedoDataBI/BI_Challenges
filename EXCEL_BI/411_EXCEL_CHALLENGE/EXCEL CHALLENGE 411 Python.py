# # Excel BIExcel BI https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7173528233966080000-8Jvu?utm_source=share&utm_medium=member_desktop
# Import necessary libraries: pandas for data manipulation and shlex for intelligent string splitting
import pandas as pd
import shlex

# Specify the path to the Excel file containing the data
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_411 - Split String at other than Space.xlsx"

# Read the Excel file into a pandas DataFrame, specifically importing only column "A"
df_pandas = pd.read_excel(file_path, usecols="A")

# Define a function to split text into parts, ignoring quoted sections
def split_ignoring_quotes(text):
    try:
        # Attempt to split the text using shlex, which respects quotes
        parts = shlex.split(text)
        return parts
    except Exception as e:
        # If an error occurs during splitting, return the original text as a list
        return [text]

# Apply the defined function to the first (and only) column, storing the split results in a new column
df_pandas['split_text'] = df_pandas.iloc[:, 0].apply(split_ignoring_quotes)

# Determine the maximum number of columns needed by finding the largest list size in 'split_text'
num_columns = df_pandas['split_text'].apply(len).max()

# Create new columns for each part of the split text
for i in range(num_columns):
    col_name = f'Sentences_{i+1}'  # Dynamically generate column names
    # Extract elements from the lists in 'split_text', padding with None if the list is too short
    df_pandas[col_name] = df_pandas['split_text'].apply(lambda x: x[i] if i < len(x) else None)

# Drop the temporary 'split_text' column, as it's no longer needed
df_pandas.drop(columns=['split_text'], inplace=True)

df_pandas
