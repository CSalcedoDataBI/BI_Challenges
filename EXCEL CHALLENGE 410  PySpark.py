from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType
import pandas as pd

# Initialize spark Session
spark = SparkSession.builder.appName("Excela_Challenge").getOrCreate()

# Define a function to convert numbers to Roman numerals
def to_roman(num):
    val =[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX","V", "IV","I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num
# Define a function to check if a string is palindrome
def is_palindrome(s):
    return s == s[::-1]

# Register the function as UDF
ronan_udf = udf(to_roman, StringType())
palindrone_udf = udf(is_palindrome, StringType())

# Define the path to your Excel file
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_410 - Palindromic Roman Numerals.xlsx"
# Use pandas to read the Excel file
df_pandas = pd.read_excel( file_path,usecols=[0] ,header=1)

# Convert the pandas a DataFrame to a Spark DataFrame
df_spark = spark.createDataFrame( df_pandas )
# add a column with the Roman numeral
df_spark = df_spark.withColumn("Roman Numeral", roman_udf(col("Decimal Number")))
# add a column indicating if the numeral is a palindrome
df_spark = df_spark.withColumn( "Is_Palindrone", palindrome_udf(col("Roman Numeral"))).filter(col("Is_Palindrone")=='true').drop("Is_Palindrone")

df_spark.show()
