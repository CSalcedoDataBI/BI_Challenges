#https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7173890586880458752-rEx5?utm_source=share&utm_medium=member_desktop
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StructType, StructField, IntegerType
import pandas as pd

spark_session = SparkSession.builder.appName("Challenge411").getOrCreate()

excel_file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_412 - Square Sum Iterate till a Single Digit .xlsx"
pandas_df = pd.read_excel(excel_file_path, usecols=[0], header=1)
spark_df = spark_session.createDataFrame(pandas_df)
# Definir el esquema para los datos resultantes de la UDF
result_schema = StructType([
    StructField("FinalSingleDigit", IntegerType(), nullable=False),
    StructField("NumberOfIterations", IntegerType(), nullable=False)
])

# Definir la función UDF que incluye el procesamiento de números de un solo dígito
def calculate_final_digit_and_iterations(number):
    iterations = 0
    # Procesar el número al menos una vez si es de un solo dígito.
    number = sum(int(digit) ** 2 for digit in str(number))
    if number < 10:
        return (number, 1)  # Retorna después de una iteración si ya es un dígito único.
    while number >= 10:
        number = sum(int(digit) ** 2 for digit in str(number))
        iterations += 1
    return (number, iterations + 1)  # +1 para contar la primera iteración para dígitos únicos.

# Registrar la función como una UDF con el esquema de resultado
calculate_udf = udf(calculate_final_digit_and_iterations, result_schema)

# Suponiendo que 'spark_df' es tu DataFrame de Spark que contiene los números a procesar
# y que hay una columna "Number" con los números a procesar

# Aplicar la UDF para procesar cada número y dividir los resultados en dos nuevas columnas
processed_df = spark_df.withColumn("Result", calculate_udf(col("Number"))) \
                       .select(
                           "Number",
                           col("Result.FinalSingleDigit").alias("Final Single Digit"),
                           col("Result.NumberOfIterations").alias("Number of Iterations")
                       )

# Mostrar los resultados
processed_df.show()
