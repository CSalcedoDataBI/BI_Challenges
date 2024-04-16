from pyspark.sql import SparkSession
from pyspark.sql.functions import min, max, col, explode, array
import pandas as pd

spark = SparkSession.builder.appName("CHALLENGE408").getOrCreate()
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_418 - Pivot on Min and Max .xlsx"
df_pandas = pd.read_excel(file_path, usecols=[0, 1, 2])

# Convertir la columna de tiempo a cadena
df_pandas['Time'] = df_pandas['Time'].astype(str)

# Crear DataFrame de Spark a partir del DataFrame de pandas
df_spark = spark.createDataFrame(df_pandas)

# Agrupar y calcular el tiempo mínimo y máximo
grouped_df = df_spark.groupBy("Date", "Emp ID") \
                     .agg(min("Time").alias("Min Time"), max("Time").alias("Max Time"))

# Expandir los tiempos mínimo y máximo en filas separadas y eliminar las columnas originales de tiempo mínimo y máximo
expanded_df = grouped_df.withColumn("Min Max", explode(array(col("Min Time"), col("Max Time")))) \
                        .drop("Min Time", "Max Time")

# Ordenar el resultado final
sorted_df = expanded_df.orderBy("Date", "Emp ID")
sorted_df.show()
