from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id, col, udf
from pyspark.sql.types import StringType
import pandas as pd

spark_session = SparkSession.builder.appName("Challenge416").getOrCreate()

excel_file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_416 - Outline Numbering.xlsx"
pandas_df = pd.read_excel(excel_file_path, usecols=[0], header=0)
spark_df = spark_session.createDataFrame(pandas_df)
df = spark_df.withColumn("id", monotonically_increasing_id())
rows = df.orderBy("id").collect()

def hierarchical_numbering(rows):
    result = []
    counters = [0] * (max(len(row['Strings']) for row in rows) + 1)
    
    for row in rows:
        level = len(row['Strings'])
        counters[level] += 1
        for l in range(level + 1, len(counters)):
            counters[l] = 0
        number = '.'.join(str(counters[l]) for l in range(1, level + 1))
        result.append((row['Strings'], number))
    return result

numbered_rows = hierarchical_numbering(rows)
df_numbered = spark.createDataFrame(numbered_rows, ["Strings", "Answer Expected"])

df_numbered.show()