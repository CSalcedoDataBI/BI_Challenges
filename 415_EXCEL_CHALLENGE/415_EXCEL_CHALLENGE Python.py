# My solution using #Python in a #Notebook in #Fabric. See the code in my repository: https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7175702542939549697-smzf?utm_source=share&utm_medium=member_desktop
import pandas as pd

def is_cyclops(n):
    s = str(n)
    length = len(s)
    if length % 2 == 0 or length < 3:
        return False
    middle_index = length // 2
    return s[middle_index] == '0' and '0' not in s[:middle_index] + s[middle_index+1:]

num_range = pd.DataFrame({'id': range(1, 10000)})  
num_range['Expected Number'] = num_range['id'] * (num_range['id'] + 1) // 2

cyclops_triangular_numbers = num_range[num_range['Expected Number'].apply(is_cyclops)].drop('id', axis=1)

print(cyclops_triangular_numbers.head(100))