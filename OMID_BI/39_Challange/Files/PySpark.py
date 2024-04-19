from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, collect_set, array
import pandas as pd

spark = SparkSession.builder.appName("UniqueValuesExtraction").getOrCreate()
file_path = "/lakehouse/default/Files/ChallengeOmid/CH-039 Transformation.xlsx"
pandas_df = pd.read_excel(file_path, usecols=[1, 2, 3, 4], nrows=8)

df = spark.createDataFrame(pandas_df)
df_exploded = df.withColumn("Result - Unique Code", explode(array(*df.columns)))

unique_values = df_exploded.select("Result - Unique Code").na.drop() \
                         .distinct().sort("Result - Unique Code")
unique_values.show()
