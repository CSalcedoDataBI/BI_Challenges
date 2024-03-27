# 419_EXCEL_CHALLENGE

Este repositorio contiene mis soluciones al 419 Excel Challenge, tal como se describe en el reto original proporcionado por Excel BI en su LinkedIn.

## Descripción del Desafío

El desafío requiere:
Invertir un número. Si este nuevo número es perfectamente divisible por el número original y ambos números no son números palíndromos, entonces enumere ese número. (Estamos excluyendo los números de palíndromo, ya que el número invertido es igual al número original)
Enumere los primeros 12 números de este tipo. Los dígitos mínimos deben ser 2.
Ejemplo: 2178. El número invertido es 8712. 8712 / 2178 = 4 y estos dos números no son números de palíndromo.

![Descripción del desafío](https://github.com/cristobalsalcedo90/BI_Challenges/blob/c9961e9a15f3befbee69580e10b67febac26e815/418_EXCEL_CHALLENGE/Files/ExcelBi.png)

La fuente del desafío puede encontrarse en el perfil de LinkedIn de Excel BI: [Excel BI LinkedIn Post](https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7177876857915117569-cHiT?utm_source=share&utm_medium=member_desktop)

## Soluciones

### Solución usando PySpark 🚀 en un Notebook en MicrosoftFabric

Aquí muestro cómo abordé el desafío usando PySpark, destacando el procesamiento distribuido para manejar datos a gran escala.

![Solución PySpark](https://github.com/cristobalsalcedo90/BI_Challenges/blob/5753259fc5fc8b86223c736ce1d6643d8aba15f3/419_EXCEL_CHALLENGE/Files/419_EXCEL_CHALLENGE_PySpark.png)

Copiar Codigo aquí:
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import IntegerType, BooleanType

# Initialize SparkSession
spark = SparkSession.builder.appName("Find Numbers").getOrCreate()

# Define UDF to check if a number is a palindrome
is_palindrome_udf = udf(lambda num: str(num) == str(num)[::-1], BooleanType())

# Define UDF to reverse a number
reverse_number_udf = udf(lambda num: int(str(num)[::-1]), IntegerType())

# Create a DataFrame of numbers to evaluate. Assuming a wide range and then we'll filter.
numbers_df = spark.range(10, 100000000).toDF("number")  # Now up to 100,000,000

# Apply UDFs to add reversed number column and filter based on conditions
filtered_df = numbers_df.withColumn("reversed", reverse_number_udf("number")) \
                        .filter(~is_palindrome_udf("number")) \
                        .filter(~is_palindrome_udf("reversed")) \
                        .filter(col("reversed") % col("number") == 0)

# Since Spark operates in a distributed manner, we cannot simply take the first 12 elements directly after filtering.
# A more efficient approach for large datasets is to use show() for direct visualization instead of collecting the data.
print("The first 12 valid numbers are:")
filtered_df.select("number").limit(12).show()

```

### Solución usando Python en un Notebook en MicrosoftFabric

Aquí está mi solución implementada en Python puro, aprovechando las bibliotecas de análisis de datos para una solución eficiente y escalable.

![Solución Python](https://github.com/cristobalsalcedo90/BI_Challenges/blob/5753259fc5fc8b86223c736ce1d6643d8aba15f3/419_EXCEL_CHALLENGE/Files/419_EXCEL_CHALLENGE_Python.png)

Copiar Codigo aquí:
```
def is_palindrome(number):
  
    return str(number) == str(number)[::-1]

valid_numbers = []
current_number = 10 

while len(valid_numbers) < 12:
    reversed_number = int(str(current_number)[::-1])
    if reversed_number % current_number == 0 and not is_palindrome(current_number) and not is_palindrome(reversed_number):
        valid_numbers.append(current_number)
    current_number += 1

print("Expected Answer:")
for number in valid_numbers:
    print(number)

```
## ¿Cómo utilizar este repositorio?

Puede clonar este repositorio y ejecutar los notebooks proporcionados para ver cómo se implementaron las soluciones. Se proporcionan instrucciones detalladas dentro de cada notebook.

## Contacto

Si tienes alguna pregunta o deseas conectarte, no dudes en visitar mi perfil de LinkedIn.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Cristobal%20Salcedo-blue)](https://www.linkedin.com/in/cristobal-salcedo)

---

Recuerda reemplazar los enlaces y las descripciones con la información correcta y actualizada. Este código markdown puede ser colocado directamente en tu archivo README.md en GitHub para presentar tu solución de una manera estructurada y profesional.
