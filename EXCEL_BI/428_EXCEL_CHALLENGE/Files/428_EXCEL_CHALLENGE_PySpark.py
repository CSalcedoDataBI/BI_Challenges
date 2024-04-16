from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import BooleanType
from datetime import datetime
spark = SparkSession.builder.appName("CHALLENGE428").getOrCreate()
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_428 - Chinese National ID.xlsx"
pandas_df = pd.read_excel(file_path, usecols=[0], nrows=10)
spark_df = spark.createDataFrame(pandas_df)
general_pattern = "\\d{6}\\d{8}\\d{3}[0-9X]"
def is_valid_date(ID):
    date_str = ID[6:14]
    try:
        datetime.strptime(date_str, "%Y%m%d")
        return True
    except ValueError:
        return False
def is_ID_valid(ID):
    base = [int(digit) for digit in ID[:17]]
    I = list(range(18, 1, -1))
    WI = [2**(i-1) % 11 for i in I]
    S = sum(digit * weight for digit, weight in zip(base, WI))
    C = (12 - (S % 11)) % 11
    C = 'X' if C == 10 else str(C)

    whole_id = ''.join(map(str, base)) + C
    return whole_id == ID
is_valid_date_udf = udf(is_valid_date, BooleanType())
is_ID_valid_udf = udf(is_ID_valid, BooleanType())
filtered_data = spark_df.filter(col("National ID").rlike(general_pattern)) \
                        .withColumn("Is Valid Date", is_valid_date_udf(col("National ID"))) \
                        .withColumn("Is ID Valid", is_ID_valid_udf(col("National ID"))) \
                        .filter(col("Is Valid Date") & col("Is ID Valid")) \
                        .drop("Is Valid Date", "Is ID Valid") \
                        .withColumnRenamed("National ID", "My Solution")
filtered_data.show()
