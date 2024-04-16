# My solution using #Pyspark in a #Notebook in #Fabric. See the code in my repository: https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7175702542939549697-smzf?utm_source=share&utm_medium=member_desktop
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import BooleanType, LongType


spark = SparkSession.builder.appName("CyclopsTriangularNumbers").getOrCreate()


def is_cyclops(n):
    s = str(n)
    length = len(s)
    if length % 2 == 0 or length < 3:
        return False
    middle_index = length // 2
    return s[middle_index] == '0' and '0' not in s[:middle_index] + s[middle_index+1:]

is_cyclops_udf = udf(is_cyclops, BooleanType())
num_range = spark.range(1, 10000) 
triangular_numbers = num_range.withColumn("Expected Number", (col("id") * (col("id") + 1) / 2).cast(LongType()))
cyclops_triangular_numbers = triangular_numbers.filter(is_cyclops_udf("Expected Number")).drop("id")
cyclops_triangular_numbers.show(100)