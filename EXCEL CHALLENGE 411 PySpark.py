# # Excel BIExcel BI https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7173528233966080000-8Jvu?utm_source=share&utm_medium=member_desktop
# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, StringType
import shlex
import pandas as pd  # Added missing import for reading Excel files

# Initialize Spark session
spark = SparkSession.builder.appName("ExcelBi411").getOrCreate()

# Define the file path to the Excel file
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_411 - Split String at other than Space.xlsx"

# Read the Excel file into a pandas DataFrame, selecting only column "A"
df_pandas = pd.read_excel(file_path, usecols="A")

# Convert the pandas DataFrame to a Spark DataFrame for further processing
df_spark = spark.createDataFrame(df_pandas)

# Define a function to split text while ignoring quotes
def split_ignoring_quotes(text):
    try:
        # Attempt to split the text using shlex to handle quotes properly
        parts = shlex.split(text)
        return parts
    except Exception as e:
        # In case of any error, return the original text as a single-element list
        return [text]

# Register the function above as a UDF (User Defined Function) in Spark
# This allows it to be used in DataFrame transformations
split_ignoring_quotes_udf = udf(split_ignoring_quotes, ArrayType(StringType()))

# Apply the UDF to the 'Sentences' column of the DataFrame
# The result is a new column ('split_text') with the text split into an array
df_result = df_spark.withColumn("split_text", split_ignoring_quotes_udf("Sentences"))

# Assuming the number of columns to create from the split text is known (e.g., 5)
num_columns = 5
for i in range(num_columns):
    # Dynamically generate new column names based on the split text
    col_name = f"Sentences_{i+1}"
    # Extract each element of the split array into its own column
    df_result = df_result.withColumn(col_name, df_result["split_text"].getItem(i))

# Remove the temporary 'split_text' column as it's no longer needed
df_result = df_result.drop("split_text")

# Display the final DataFrame, showing all generated columns
df_result.show(truncate=False)
