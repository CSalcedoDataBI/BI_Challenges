import pandas as pd
from datetime import datetime

file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_428 - Chinese National ID.xlsx"
pandas_df = pd.read_excel(file_path, usecols=[0], nrows=10)

general_pattern = "\\d{6}\\d{8}\\d{3}[0-9X]"

def is_valid_date(ID):
    date_str = ID[6:14]
    try:
        datetime.strptime(date_str, "%Y%m%d")
        return True
    except ValueError:
        return False

def is_ID_valid(ID):
    base = [int(digit) for digit in ID[:17]]
    I = list(range(18, 1, -1))
    WI = [2**(i-1) % 11 for i in I]
    S = sum(digit * weight for digit, weight in zip(base, WI))
    C = (12 - (S % 11)) % 11
    C = 'X' if C == 10 else str(C)

    whole_id = ''.join(map(str, base)) + C
    return whole_id == ID
filtered_data = pandas_df[pandas_df['National ID'].str.match(general_pattern).fillna(False)].copy()
filtered_data['My Solution'] = filtered_data['National ID'].apply(lambda x: x if is_valid_date(x) and is_ID_valid(x) else pd.NA)

filtered_data.drop(columns=['National ID'], inplace=True)
filtered_data = filtered_data.dropna(subset=['My Solution'])