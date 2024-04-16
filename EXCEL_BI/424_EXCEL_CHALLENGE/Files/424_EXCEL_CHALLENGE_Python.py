import pandas as pd
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_424 - Insert In Between Multiplication.xlsx"

pandas_df = pd.read_excel(file_path, usecols=[0, 1])
def apply_logic(number):
    number_str = str(number)
    result = number_str[0]  
    for i in range(len(number_str) - 1):
        digit1 = int(number_str[i])
        digit2 = int(number_str[i + 1])
        result += str(digit1 * digit2) + number_str[i + 1]
    return result

pandas_df['mySolution'] = pandas_df['Words'].apply(apply_logic)
print(pandas_df)