from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Iniciar SparkSession (asumiendo que ya está iniciado y asignado a la variable `spark`)
spark = SparkSession.builder.appName("EXCELBICHALLLENGE422").getOrCreate()

# Crear un DataFrame con el rango de años
years_df = spark.range(1901, 10000).toDF("year")

# Definir las reglas de años bisiestos para ambos calendarios como columnas calculadas
years_df = years_df.withColumn(
    "is_gregorian_leap",
    expr("((year % 4 = 0) AND (year % 100 != 0)) OR (year % 400 = 0)")
).withColumn(
    "is_revised_julian_leap",
    expr("((year % 4 = 0) AND (year % 100 != 0)) OR (year % 900 = 200) OR (year % 900 = 600)")
)

# Filtrar los años donde los calendarios no están de acuerdo en si es un año bisiesto
disagreement_years_df = years_df.filter(
    "is_gregorian_leap != is_revised_julian_leap"
)

# Mostrar los resultados
disagreement_years_df.select("year").show()