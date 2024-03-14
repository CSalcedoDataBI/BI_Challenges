# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7173890586880458752-rEx5?utm_source=share&utm_medium=member_desktop
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StructType, StructField, IntegerType
import pandas as pd

# Initialize a Spark session for distributed data processing.
spark_session = SparkSession.builder.appName("DigitSumChallenge").getOrCreate()

# Specify the path to the Excel file that contains the data.
excel_file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_412 - Square Sum Iterate till a Single Digit .xlsx"

# Load the specified columns of the Excel file into a Pandas DataFrame.
pandas_df = pd.read_excel(excel_file_path, usecols=[0], header=1)

# Convert the Pandas DataFrame into a Spark DataFrame for distributed processing.
spark_df = spark_session.createDataFrame(pandas_df)

# Define a schema for the structured data returned by the custom Spark UDF.
# This includes fields for the final digit and the number of iterations needed.
result_schema = StructType([
    StructField("FinalSingleDigit", IntegerType(), nullable=False),
    StructField("NumberOfIterations", IntegerType(), nullable=False)
])

# Define a User-Defined Function (UDF) to perform the digit squaring and summing operation.
def calculate_final_digit_and_iterations(number):
    iterations = 0
    while number >= 10:
        # Sum the squares of each digit in the number.
        number = sum(int(digit) ** 2 for digit in str(number))
        iterations += 1
    return number, iterations

# Register the UDF with Spark, specifying the output schema.
calculate_udf = udf(calculate_final_digit_and_iterations, result_schema)

# Apply the UDF to each row in the 'Number' column of the Spark DataFrame, and create new columns
# for the final single digit and the number of iterations.
processed_df = spark_df.withColumn("Result", calculate_udf(col("Number"))) \
                       .select(
                           "Number",
                           col("Result.FinalSingleDigit").alias("Final Single Digit"),
                           col("Result.NumberOfIterations").alias("Number of Iterations")
                       )

# Display the processed DataFrame, showing the original number, its final digit, and iteration count.
processed_df.show()
