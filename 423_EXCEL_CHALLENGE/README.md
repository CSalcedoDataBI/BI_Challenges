# 423_EXCEL_CHALLENGE

Este repositorio contiene mis soluciones al 423 Excel Challenge, tal como se describe en el reto original proporcionado por Excel BI en su LinkedIn.

## Descripción del Desafío

El desafío requiere:
Divida las cadenas dadas cada vez que se produzca un cambio entre el alfabeto inglés y los números. Este es un problema que distingue entre mayúsculas y minúsculas. Por lo tanto, la división ocurrirá si el cambio es par para el caso.
Ej. dBaw46c8 - d, B, aw, 46, c, 8

![Descripción del desafío](https://github.com/cristobalsalcedo90/BI_Challenges/blob/80c4648637d0a83a29a496cdfa8256e267417033/423_EXCEL_CHALLENGE/Files/ExcelBi.png)

La fuente del desafío puede encontrarse en el perfil de LinkedIn de Excel BI: [Excel BI LinkedIn Post](https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7179326423331921920-tw8v?utm_source=share&utm_medium=member_desktop)

## Soluciones

### Solución usando PySpark 🚀 en un Notebook en MicrosoftFabric

Aquí muestro cómo abordé el desafío usando PySpark, destacando el procesamiento distribuido para manejar datos a gran escala.

![Solución PySpark](https://github.com/cristobalsalcedo90/BI_Challenges/blob/80c4648637d0a83a29a496cdfa8256e267417033/423_EXCEL_CHALLENGE/Files/423_EXCEL_CHALLENGE_PySpark.png)

Copiar Codigo aquí:
```python
from pyspark.sql import SparkSession 
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, StringType
import re
import pandas as pd

# Initialize Spark session
spark = SparkSession.builder.appName("Challenge423").getOrCreate()

# Regular expression to match transitions between lower and uppercase letters, and between letters and digits
transition_regex = (
    r'(?<=[a-z])(?=[A-Z])|'  # Lowercase to uppercase
    r'(?<=[A-Z])(?=[a-z])|'  # Uppercase to lowercase
    r'(?<=[A-Za-z])(?=\d)|'  # Letters to digits
    r'(?<=\d)(?=[A-Za-z])'   # Digits to letters
)

# Path to the input Excel file
excel_file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_423 - Split Case Sensitive Alphabets and Numbers.xlsx"

# Load the Excel file into a Pandas DataFrame
pandas_dataframe = pd.read_excel(excel_file_path, usecols=[0])

# Convert the Pandas DataFrame to a Spark DataFrame
spark_dataframe = spark.createDataFrame(pandas_dataframe)

# Function to split strings based on the defined transitions
def split_string_on_transition(input_string):
    return re.split(transition_regex, input_string)

# Register the function as a Spark UDF
split_on_transition_udf = udf(split_string_on_transition, ArrayType(StringType()))

# Apply the UDF to the Spark DataFrame to create a new column with the expected answer
result_dataframe = spark_dataframe.select("Data", split_on_transition_udf("Data").alias("ExpectedAnswer"))

# Display the results without truncating the output
result_dataframe.show(truncate=False)

```

### Solución usando Python en un Notebook en MicrosoftFabric

Aquí está mi solución implementada en Python puro, aprovechando las bibliotecas de análisis de datos para una solución eficiente y escalable.

![Solución Python](https://github.com/cristobalsalcedo90/BI_Challenges/blob/80c4648637d0a83a29a496cdfa8256e267417033/423_EXCEL_CHALLENGE/Files/423_EXCEL_CHALLENGE_Python.png)

Copiar Codigo aquí:
```python
import pandas as pd
import re

# Path to the Excel file
excel_file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_423 - Split Case Sensitive Alphabets and Numbers.xlsx"

# Load the Excel file into a Pandas DataFrame
pandas_dataframe = pd.read_excel(excel_file_path, usecols=[0])

# Regular expression to identify transitions
transition_regex = (
    r'(?<=[a-z])(?=[A-Z])|'  # Lowercase to uppercase
    r'(?<=[A-Z])(?=[a-z])|'  # Uppercase to lowercase
    r'(?<=[A-Za-z])(?=\d)|'  # Letters to digits
    r'(?<=\d)(?=[A-Za-z])'   # Digits to letters
)

# Function to split strings based on defined transitions
def split_string_on_transition(input_string):
    return re.split(transition_regex, input_string)

# Apply the function to the DataFrame
pandas_dataframe['ExpectedAnswer'] = pandas_dataframe['Data'].apply(split_string_on_transition)

# Display the DataFrame
print(pandas_dataframe)

```
## ¿Cómo utilizar este repositorio?

Puede clonar este repositorio y ejecutar los notebooks proporcionados para ver cómo se implementaron las soluciones. Se proporcionan instrucciones detalladas dentro de cada notebook.

## Contacto

Si tienes alguna pregunta o deseas conectarte, no dudes en visitar mi perfil de LinkedIn.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Cristobal%20Salcedo-blue)](https://www.linkedin.com/in/cristobal-salcedo)

---

Recuerda reemplazar los enlaces y las descripciones con la información correcta y actualizada. Este código markdown puede ser colocado directamente en tu archivo README.md en GitHub para presentar tu solución de una manera estructurada y profesional.
