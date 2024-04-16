import pandas as pd

path_file = "/lakehouse/default/Files/ChallengeOmid/CH-036 Pareto Line.xlsx"

pandas_df = pd.read_excel(path_file, header=1, usecols=[1, 2, 3, 4])
result = pandas_df.apply(
    lambda row: not any((pandas_df.iloc[:, 1:4] > row[1:4]).all(axis=1)), axis=1
)
result = pandas_df.apply(
    lambda row: not any((pandas_df.iloc[:, 1:4] > row[1:4]).all(axis=1)), axis=1
)
result = (
    result[result].index.to_frame(index=False).rename(columns={0: "Solution ID"}) + 1
)
result["Solution ID"] = result["Solution ID"].astype(int)
print(result)
