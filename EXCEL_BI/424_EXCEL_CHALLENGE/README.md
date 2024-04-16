# 424_EXCEL_CHALLENGE

Este repositorio contiene mis soluciones al 424 Excel Challenge, tal como se describe en el reto original proporcionado por Excel BI en su LinkedIn.

## Descripción del Desafío

El desafío requiere:
Toma los dígitos i-ésimos y (i+1), multiplícalos e inserta el resultado entre los mismos dígitos.
Ej. 2905
2*9 = 18 => 2189 
9*0 = 0 => 218900
0*5 = 0 => 21890005

![Descripción del desafío](https://github.com/cristobalsalcedo90/BI_Challenges/blob/a3009c9b15d2c8c8d28ba065d8c286b4167a2e5a/424_EXCEL_CHALLENGE/Files/ExcelBi.png)

La fuente del desafío puede encontrarse en el perfil de LinkedIn de Excel BI: [Excel BI LinkedIn Post](https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7180413652410261504-RU-0?utm_source=share&utm_medium=member_desktop)

## Soluciones

### Solución usando PySpark 🚀 en un Notebook en MicrosoftFabric

Aquí muestro cómo abordé el desafío usando PySpark, destacando el procesamiento distribuido para manejar datos a gran escala.

![Solución PySpark](https://github.com/cristobalsalcedo90/BI_Challenges/blob/a3009c9b15d2c8c8d28ba065d8c286b4167a2e5a/424_EXCEL_CHALLENGE/Files/424_EXCEL_CHALLENGE_PySpark.png)

Copiar Codigo aquí:
```python
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

```

### Solución usando Python en un Notebook en MicrosoftFabric

Aquí está mi solución implementada en Python puro, aprovechando las bibliotecas de análisis de datos para una solución eficiente y escalable.

![Solución Python](https://github.com/cristobalsalcedo90/BI_Challenges/blob/a3009c9b15d2c8c8d28ba065d8c286b4167a2e5a/424_EXCEL_CHALLENGE/Files/424_EXCEL_CHALLENGE_Python.png)

Copiar Codigo aquí:
```python
import pandas as pd
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_424 - Insert In Between Multiplication.xlsx"

pandas_df = pd.read_excel(file_path, usecols=[0, 1])
def apply_logic(number):
    number_str = str(number)
    result = number_str[0]  
    for i in range(len(number_str) - 1):
        digit1 = int(number_str[i])
        digit2 = int(number_str[i + 1])
        result += str(digit1 * digit2) + number_str[i + 1]
    return result

pandas_df['mySolution'] = pandas_df['Words'].apply(apply_logic)
print(pandas_df)

```
## Agradecimientos y Referencias
Un agradecimiento especial a la comunidad de [Excel BI](https://www.linkedin.com/in/excelbi/) por proporcionar estos desafiantes y enriquecedores problemas que nos permiten crecer profesionalmente en el campo del BI.

## ¿Cómo utilizar este repositorio?

Puede clonar este repositorio y ejecutar los notebooks proporcionados para ver cómo se implementaron las soluciones. Se proporcionan instrucciones detalladas dentro de cada notebook.

## Contacto

Si tienes alguna pregunta o deseas conectarte, no dudes en visitar mi perfil de LinkedIn.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Cristobal%20Salcedo-blue)](https://www.linkedin.com/in/cristobal-salcedo)

---

Recuerda reemplazar los enlaces y las descripciones con la información correcta y actualizada. Este código markdown puede ser colocado directamente en tu archivo README.md en GitHub para presentar tu solución de una manera estructurada y profesional.
