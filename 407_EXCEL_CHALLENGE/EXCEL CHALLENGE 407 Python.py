import pandas as pd

# Path to the Excel file to be read
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_407 - Mirror Cipher.xlsx"

# Load the Excel file into a Pandas DataFrame, using only columns "A" and "B"
df = pd.read_excel(file_path, usecols="A:B")

# Definition of the encryption function
def mirror_cipher_caesar_shift(plaintext, shift):
    """
    This function applies a mirror cipher followed by a Caesar cipher.
    
    - First, it reverses the order of the words and then reverses the letters within each word.
    - Then it applies a Caesar shift with the given value.
    
    Parameters:
    - plaintext: The original text to be encrypted.
    - shift: Shift value for the Caesar cipher.
    
    Returns:
    - Encrypted text applying the mirror cipher first and then the Caesar cipher.
    """
    # Reverse the order of the words
    words_reversed = plaintext.split()[::-1]
    # Reverse the letters within each word
    mirrored_sentence = ' '.join(word[::-1] for word in words_reversed)
    # Apply the Caesar cipher
    encrypted_sentence = ''.join(
        chr(((ord(char) - 65 + shift) % 26) + 65) if char.isupper() else
        chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else char
        for char in mirrored_sentence
    )
    return encrypted_sentence

# Apply the encryption function to each row of the DataFrame
df['Encrypted'] = df.apply(lambda row: mirror_cipher_caesar_shift(row['Plain Text'], row['Shift']), axis=1)

# Display the DataFrame with the results
print(df)
