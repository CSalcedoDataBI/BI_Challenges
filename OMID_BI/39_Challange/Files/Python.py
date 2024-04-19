import pandas as pd
file_path = "/lakehouse/default/Files/ChallengeOmid/CH-039 Transformation.xlsx"
df = pd.read_excel(file_path, usecols=[1, 2, 3, 4], nrows=8)
df_melted = df.melt(var_name='Attribute', value_name='Result - Unique Code')
unique_values = pd.Series(df_melted['Result - Unique Code'].dropna() \
                .unique()).sort_values().tolist()
result_df = pd.DataFrame({"Result - Unique Code": unique_values})
print(result_df)