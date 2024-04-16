from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import pandas as pd

# Ruta del archivo
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_424 - Insert In Between Multiplication.xlsx"

# Leer el archivo Excel en un DataFrame de Pandas
pandas_df = pd.read_excel(file_path, usecols=[0, 1])

# Crear un DataFrame de Spark a partir del DataFrame de Pandas
spark_df = spark.createDataFrame(pandas_df)

# Definir la función que realiza la lógica deseada
def apply_logic(number):
    """
    Esta función toma un número entero y aplica la lógica deseada, que es multiplicar
    cada par de dígitos consecutivos y insertar el resultado entre ellos.
    
    Args:
        number (int): Número entero a ser procesado.
        
    Returns:
        str: Número procesado según la lógica especificada.
    """
    number_str = str(number)
    result = number_str[0]  # Tomamos el primer dígito como parte del resultado
    for i in range(len(number_str) - 1):
        digit1 = int(number_str[i])
        digit2 = int(number_str[i + 1])
        result += str(digit1 * digit2) + number_str[i + 1]
    return result

# Registra la función de usuario (UDF)
apply_logic_udf = udf(apply_logic, StringType())

# Aplica la UDF a la columna deseada en tu DataFrame
result_df = spark_df.withColumn("mySolution", apply_logic_udf("Words"))

# Mostrar el DataFrame resultante
result_df.show(truncate=False)
