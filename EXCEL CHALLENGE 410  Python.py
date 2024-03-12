import pandas as pd

def to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def is_palindrome(s):
    return s == s[::-1]

file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_410 - Palindromic Roman Numerals.xlsx"

df = pd.read_excel(file_path, usecols=[0], header=1)

df['Roman Numeral'] = df.apply(lambda row: to_roman(row[df.columns[0]]), axis=1)
df['Is Palindrome'] = df['Roman Numeral'].apply(is_palindrome)

result_df = df[df['Is Palindrome'] == True]

final_df = result_df[['Decimal Number', 'Roman Numeral']]

print(final_df)
