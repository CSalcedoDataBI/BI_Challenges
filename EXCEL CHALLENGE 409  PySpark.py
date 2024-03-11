# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7172803509036290048-2cU-?utm_source=share&utm_medium=member_desktop
# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, split, last, monotonically_increasing_id
from pyspark.sql.window import Window
import pandas as pd

# Initialize SparkSession
spark = SparkSession.builder.appName("fill_down_example").getOrCreate()

# Specify the file path to the Excel file
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_409 - Table_Regular.xlsx"

# Read the Excel file into a Pandas DataFrame, using only columns A through E
df_pandas = pd.read_excel(file_path, usecols="A:E")

# Convert the Pandas DataFrame into a Spark DataFrame
spark_df = spark.createDataFrame(df_pandas)

# Split the 'Items' column by commas and then explode it to create a new row for each item
spark_df1 = spark_df.withColumn("Items", split(col("Items"), ","))
spark_df2 = spark_df1.withColumn("Items", explode("Items"))

# Add a unique identifier 'row_id' to each row to preserve the order after exploding 'Items'
spark_df2 = spark_df2.withColumn("row_id", monotonically_increasing_id())

# Define a window specification to use for filling down nulls, ordered by 'row_id'
windowSpec = Window.orderBy("row_id").rowsBetween(Window.unboundedPreceding, Window.currentRow)

# Apply fill down for 'Categories' and 'Note' columns using the last known non-null value in each column
spark_df_filled = spark_df2.withColumn("Categories", last("Categories", ignorenulls=True).over(windowSpec))\
                           .withColumn("Note", last("Note", ignorenulls=True).over(windowSpec))

# Drop the 'row_id' column as it's no longer needed after fill down operation
spark_df_final = spark_df_filled.drop("row_id")

# Show the final DataFrame, with 'Categories' and 'Note' columns filled down
spark_df_final.show(truncate=False)
