import pandas as pd
import re

# Path to the Excel file
excel_file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_423 - Split Case Sensitive Alphabets and Numbers.xlsx"

# Load the Excel file into a Pandas DataFrame
pandas_dataframe = pd.read_excel(excel_file_path, usecols=[0])

# Regular expression to identify transitions
transition_regex = (
    r'(?<=[a-z])(?=[A-Z])|'  # Lowercase to uppercase
    r'(?<=[A-Z])(?=[a-z])|'  # Uppercase to lowercase
    r'(?<=[A-Za-z])(?=\d)|'  # Letters to digits
    r'(?<=\d)(?=[A-Za-z])'   # Digits to letters
)

# Function to split strings based on defined transitions
def split_string_on_transition(input_string):
    return re.split(transition_regex, input_string)

# Apply the function to the DataFrame
pandas_dataframe['ExpectedAnswer'] = pandas_dataframe['Data'].apply(split_string_on_transition)

# Display the DataFrame
print(pandas_dataframe)
