import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Define the double accumulate cipher logic as a Python function
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

# Register the Python function as a UDF (User Defined Function) in PySpark
double_accumulate_cipher_udf = udf(double_accumulate_cipher, StringType())

# File path
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_427 - Double Accumulative Cipher.xlsx"

# Read the Excel file into a Pandas DataFrame
pandas_df = pd.read_excel(file_path, nrows=9)

# Create a SparkSession
spark = SparkSession.builder.appName("DoubleAccumulateCipher").getOrCreate()

# Convert the Pandas DataFrame to PySpark DataFrame
spark_df = spark.createDataFrame(pandas_df)

# Apply the UDF to the DataFrame and store the result in a new column
result_df = spark_df.withColumn("My Solution", double_accumulate_cipher_udf("Plain Text"))

# Show the resulting PySpark DataFrame
result_df.show(truncate=False)
