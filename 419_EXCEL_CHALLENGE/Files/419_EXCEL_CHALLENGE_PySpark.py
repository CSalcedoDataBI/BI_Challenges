from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import IntegerType, BooleanType

# Initialize SparkSession
spark = SparkSession.builder.appName("Find Numbers").getOrCreate()

# Define UDF to check if a number is a palindrome
is_palindrome_udf = udf(lambda num: str(num) == str(num)[::-1], BooleanType())

# Define UDF to reverse a number
reverse_number_udf = udf(lambda num: int(str(num)[::-1]), IntegerType())

# Create a DataFrame of numbers to evaluate. Assuming a wide range and then we'll filter.
numbers_df = spark.range(10, 100000000).toDF("number")  # Now up to 100,000,000

# Apply UDFs to add reversed number column and filter based on conditions
filtered_df = numbers_df.withColumn("reversed", reverse_number_udf("number")) \
                        .filter(~is_palindrome_udf("number")) \
                        .filter(~is_palindrome_udf("reversed")) \
                        .filter(col("reversed") % col("number") == 0)

# Since Spark operates in a distributed manner, we cannot simply take the first 18 elements directly after filtering.
# A more efficient approach for large datasets is to use show() for direct visualization instead of collecting the data.
print("The first 18 valid numbers are:")
filtered_df.select("number").limit(18).show()