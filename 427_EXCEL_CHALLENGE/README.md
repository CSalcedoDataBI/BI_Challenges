# 427_EXCEL_CHALLENGE

Este repositorio contiene mis soluciones al 427 Excel Challenge, tal como se describe en el reto original proporcionado por Excel BI en su LinkedIn.

## Descripción del Desafío

El desafío requiere:
Doble acumulación de cifrado
Paso 1. Tome una cadena y reemplace sus alfabetos con a = 0 ... z = 25 en una matriz. 
Paso 2. Realice la suma acumulativa de los elementos respectivos de la matriz donde un elemento es igual a este elemento + suma de los elementos anteriores.
Paso 3. Tome el módulo 26 de los elementos de la matriz.
Paso 4. Aplique los pasos 2 y 3 en la matriz resultante de los pasos 3.
Paso 5. Convierta la matriz en alfabetos respectivos donde 0 = a.... 25=z
Ej. caballo
Paso 1. (7, 14, 17, 18, 4)
Paso 2. (7, 21, 38, 56, 60)
Paso 3. (7, 21, 12, 4, 8)
Paso 4. (7, 28, 40, 44, 52) => aplicar módulo 26 = > (7, 2, 14, 18, 0) 
Paso 5. La respuesta sería hcosa

![Descripción del desafío](https://github.com/cristobalsalcedo90/BI_Challenges/blob/e2c941df816763045366df0658358ab82f4168ea/427_EXCEL_CHALLENGE/Files/ExcelBi.png)

La fuente del desafío puede encontrarse en el perfil de LinkedIn de Excel BI: [Excel BI LinkedIn Post](https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7181500742896115712-C75i?utm_source=share&utm_medium=member_desktop)

## Soluciones

### Solución usando PySpark 🚀 en un Notebook en MicrosoftFabric

Aquí muestro cómo abordé el desafío usando PySpark, destacando el procesamiento distribuido para manejar datos a gran escala.

![Solución PySpark](https://github.com/cristobalsalcedo90/BI_Challenges/blob/e2c941df816763045366df0658358ab82f4168ea/427_EXCEL_CHALLENGE/Files/427_EXCEL_CHALLENGE_PySpark.png)

Copiar Codigo aquí:
```python
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Define the double accumulate cipher logic as a Python function
def double_accumulate_cipher(text):
    """
    Apply double accumulation cipher to a given text.
    
    Args:
        text (str): Text to be encrypted.
        
    Returns:
        str: Encrypted text.
    """
    # Convert each letter to its position in the alphabet (a=0, b=1, ..., z=25)
    array = [ord(char.lower()) - 97 for char in text]
    
    # Perform cumulative sum and apply modulo 26
    accumulated_sum = [sum(array[:i+1]) % 26 for i in range(len(array))]
    
    # Apply cumulative sum again and apply modulo 26
    double_accumulated_sum = [sum(accumulated_sum[:i+1]) % 26 for i in range(len(accumulated_sum))]
    
    # Convert numbers back to letters
    result = ''.join(chr(num + 97) for num in double_accumulated_sum)
    
    return result

# Register the Python function as a UDF (User Defined Function) in PySpark
double_accumulate_cipher_udf = udf(double_accumulate_cipher, StringType())

# File path
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_427 - Double Accumulative Cipher.xlsx"

# Read the Excel file into a Pandas DataFrame
pandas_df = pd.read_excel(file_path, nrows=9)

# Create a SparkSession
spark = SparkSession.builder.appName("DoubleAccumulateCipher").getOrCreate()

# Convert the Pandas DataFrame to PySpark DataFrame
spark_df = spark.createDataFrame(pandas_df)

# Apply the UDF to the DataFrame and store the result in a new column
result_df = spark_df.withColumn("My Solution", double_accumulate_cipher_udf("Plain Text"))

# Show the resulting PySpark DataFrame
result_df.show(truncate=False)

```

### Solución usando Python en un Notebook en MicrosoftFabric

Aquí está mi solución implementada en Python puro, aprovechando las bibliotecas de análisis de datos para una solución eficiente y escalable.

![Solución Python](https://github.com/cristobalsalcedo90/BI_Challenges/blob/e2c941df816763045366df0658358ab82f4168ea/427_EXCEL_CHALLENGE/Files/427_EXCEL_CHALLENGE_Python.png)

Copiar Codigo aquí:
```python
import pandas as pd

def double_accumulate_cipher(text):
    """
    Apply double accumulation cipher to a given text.
    
    Args:
        text (str): Text to be encrypted.
        
    Returns:
        str: Encrypted text.
    """
    # Convert each letter to its position in the alphabet (a=0, b=1, ..., z=25)
    array = [ord(char.lower()) - 97 for char in text]
    
    # Perform cumulative sum and apply modulo 26
    accumulated_sum = [sum(array[:i+1]) % 26 for i in range(len(array))]
    
    # Apply cumulative sum again and apply modulo 26
    double_accumulated_sum = [sum(accumulated_sum[:i+1]) % 26 for i in range(len(accumulated_sum))]
    
    # Convert numbers back to letters
    result = ''.join(chr(num + 97) for num in double_accumulated_sum)
    
    return result

# File path
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_427 - Double Accumulative Cipher.xlsx"

# Read the Excel file into a Pandas DataFrame
pandas_df = pd.read_excel(file_path, nrows=9)

# Apply the function to the DataFrame and store the result in a new column
pandas_df['My Solution'] = pandas_df['Plain Text'].apply(double_accumulate_cipher)

# Display the resulting DataFrame
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
