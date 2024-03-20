import pandas as pd

excel_file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_416 - Outline Numbering.xlsx"
pandas_df = pd.read_excel(excel_file_path, usecols=[0], header=0)
max_depth = pandas_df['Strings'].apply(len).max()
counters = [0] * max_depth
def get_number(s):
    global counters
    level = len(s)
    counters[level-1] += 1
    counters[level:] = [0] * (max_depth - level)
    return '.'.join(str(counters[i]) for i in range(level) if counters[i] > 0)
pandas_df['HierarchicalNumber'] = pandas_df['Strings'].apply(get_number)

print(pandas_df)
