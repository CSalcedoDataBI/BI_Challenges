import pandas as pd

def double_accumulate_cipher(text):
    """
    Apply double accumulation cipher to a given text.
    
    Args:
        text (str): Text to be encrypted.
        
    Returns:
        str: Encrypted text.
    """
    # Convert each letter to its position in the alphabet (a=0, b=1, ..., z=25)
    array = [ord(char.lower()) - 97 for char in text]
    
    # Perform cumulative sum and apply modulo 26
    accumulated_sum = [sum(array[:i+1]) % 26 for i in range(len(array))]
    
    # Apply cumulative sum again and apply modulo 26
    double_accumulated_sum = [sum(accumulated_sum[:i+1]) % 26 for i in range(len(accumulated_sum))]
    
    # Convert numbers back to letters
    result = ''.join(chr(num + 97) for num in double_accumulated_sum)
    
    return result

# File path
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_427 - Double Accumulative Cipher.xlsx"

# Read the Excel file into a Pandas DataFrame
pandas_df = pd.read_excel(file_path, nrows=9)

# Apply the function to the DataFrame and store the result in a new column
pandas_df['My Solution'] = pandas_df['Plain Text'].apply(double_accumulate_cipher)

# Display the resulting DataFrame
print(pandas_df)
