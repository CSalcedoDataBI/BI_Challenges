# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7169179556946329600-4n_0/
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat, lit, sum as _sum, round, asc
import pandas as pd

# Path to the Excel file
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_403 - Generate Pivot Table.xlsx"
sheet_name = "Sheet1"
# Read data from Excel with Pandas
df_pandas = pd.read_excel(file_path, sheet_name=sheet_name, usecols="A:B", nrows=100)

# Start SparkSession
spark = SparkSession.builder.appName("GroupByInterval").getOrCreate()

# Convert to PySpark DataFrame
df_spark = spark.createDataFrame(df_pandas)

# Display the original DataFrame (optional)
df_spark.show(3)

# Base year for the group calculation
base_year = 1990

# Group by 5-year intervals
df_grouped = df_spark.withColumn("YearGroup", ((col("Year") - base_year) / 5).cast("int") * 5 + base_year) \
    .groupBy("YearGroup") \
    .agg(_sum("Value").alias("Sum of Value"))

# Calculate the total of all values for later percentage calculation
total_value = df_grouped.agg(_sum("Sum of Value").alias("total")).first()["total"]

# Calculate the percentage for each group and convert to integer
df_grouped = df_grouped.withColumn("% of Value", 
                                   round((col("Sum of Value") / total_value) * 100).cast("int"))

# Add the year interval labels
df_grouped = df_grouped.withColumn("Year", concat(col("YearGroup"), lit("-"), col("YearGroup") + 4)) \
    .selectExpr("Year", "`Sum of Value`", "`% of Value` || '%' as `% of Value`")

# Ensure the year groups are sorted
df_grouped = df_grouped.orderBy(asc("YearGroup"))

# Add the grand total at the end
df_grand_total = spark.createDataFrame([("Grand Total", total_value, "100%")], ["Year", "Sum of Value", "% of Value"])
df_final = df_grouped.unionByName(df_grand_total)

# Display the final result
df_final.show()
