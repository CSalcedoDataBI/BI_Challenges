from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType
import pandas as pd
spark = SparkSession.builder.appName("Excel to Spark DF").getOrCreate()
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_407 - Mirror Cipher.xlsx"

pandas_df = pd.read_excel(file_path, usecols="A:B")
spark_df = spark.createDataFrame(pandas_df)

def mirror_cipher_caesar_shift(plaintext, shift):
    words_reversed = plaintext.split()[::-1]
    mirrored_sentence = ' '.join(word[::-1] for word in words_reversed)
    encrypted_sentence = ''.join(
        chr(((ord(char) - 65 + shift) % 26) + 65) if char.isupper() else
        chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else char
        for char in mirrored_sentence
    )
    return encrypted_sentence
    
encrypt_udf = udf(mirror_cipher_caesar_shift, StringType())
df_result = spark_df.withColumn("Answer Expected", encrypt_udf(col("Plain Text"), col("Shift")))
display(df_result)
