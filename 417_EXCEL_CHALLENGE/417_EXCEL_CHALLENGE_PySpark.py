from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import re

spark = SparkSession.builder.appName("CHALLENGE417").getOrCreate()
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_417 - Split Alphabets and Numbers.xlsx"
pandas_df = pd.read_excel(file_path, usecols=[0])
spark_df = spark.createDataFrame(pandas_df)

def transform_data(value):
    parts = re.findall(r'\d+|[A-Za-z]+', value)
    return ', '.join(parts)

transform_data_udf = udf(transform_data, StringType())
df_transformed = spark_df.withColumn("ExpectedAnswer", transform_data_udf("Data"))
df_transformed.show(truncate=False)