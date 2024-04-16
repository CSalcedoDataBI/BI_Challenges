import pandas as pd
import re

file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_417 - Split Alphabets and Numbers.xlsx"
pandas_df = pd.read_excel(file_path, usecols=[0])

def transform_data(value):
    parts = re.findall(r'\d+|[A-Za-z]+', value)
    return ', '.join(parts)

pandas_df['ExpectedAnswer'] = pandas_df['Data'].apply(transform_data)
print(pandas_df)
