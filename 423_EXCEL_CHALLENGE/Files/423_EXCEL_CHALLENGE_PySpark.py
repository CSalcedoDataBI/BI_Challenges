from pyspark.sql import SparkSession 
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, StringType
import re
import pandas as pd

# Initialize Spark session
spark = SparkSession.builder.appName("Challenge423").getOrCreate()

# Regular expression to match transitions between lower and uppercase letters, and between letters and digits
transition_regex = (
    r'(?<=[a-z])(?=[A-Z])|'  # Lowercase to uppercase
    r'(?<=[A-Z])(?=[a-z])|'  # Uppercase to lowercase
    r'(?<=[A-Za-z])(?=\d)|'  # Letters to digits
    r'(?<=\d)(?=[A-Za-z])'   # Digits to letters
)

# Path to the input Excel file
excel_file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_423 - Split Case Sensitive Alphabets and Numbers.xlsx"

# Load the Excel file into a Pandas DataFrame
pandas_dataframe = pd.read_excel(excel_file_path, usecols=[0])

# Convert the Pandas DataFrame to a Spark DataFrame
spark_dataframe = spark.createDataFrame(pandas_dataframe)

# Function to split strings based on the defined transitions
def split_string_on_transition(input_string):
    return re.split(transition_regex, input_string)

# Register the function as a Spark UDF
split_on_transition_udf = udf(split_string_on_transition, ArrayType(StringType()))

# Apply the UDF to the Spark DataFrame to create a new column with the expected answer
result_dataframe = spark_dataframe.select("Data", split_on_transition_udf("Data").alias("ExpectedAnswer"))

# Display the results without truncating the output
result_dataframe.show(truncate=False)
