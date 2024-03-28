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

```

### Solución usando Python en un Notebook en MicrosoftFabric

Aquí está mi solución implementada en Python puro, aprovechando las bibliotecas de análisis de datos para una solución eficiente y escalable.

![Solución Python](https://github.com/cristobalsalcedo90/BI_Challenges/blob/5753259fc5fc8b86223c736ce1d6643d8aba15f3/419_EXCEL_CHALLENGE/Files/419_EXCEL_CHALLENGE_Python.png)

Copiar Codigo aquí:
```python
# Re-defining the functions to check leap years for both the Gregorian and Revised Julian calendars

def is_leap_gregorian(year):
    # Leap year rule for Gregorian calendar
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_leap_revised_julian(year):
    # Leap year rule for Revised Julian calendar
    return year % 4 == 0 and (year % 100 != 0 or year % 900 == 200 or year % 900 == 600)

# Initialize an empty list to store years where the leap year status disagrees
disagreement_years_list = []

# Iterate over each year in the range
for year in range(1901, 10000):
    # Check leap year status for both calendars
    gregorian = is_leap_gregorian(year)
    revised_julian = is_leap_revised_julian(year)
    
    # If the leap year status disagrees, add the year to the list
    if gregorian != revised_julian:
        disagreement_years_list.append(year)

disagreement_years_list

```
## ¿Cómo utilizar este repositorio?

Puede clonar este repositorio y ejecutar los notebooks proporcionados para ver cómo se implementaron las soluciones. Se proporcionan instrucciones detalladas dentro de cada notebook.

## Contacto

Si tienes alguna pregunta o deseas conectarte, no dudes en visitar mi perfil de LinkedIn.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Cristobal%20Salcedo-blue)](https://www.linkedin.com/in/cristobal-salcedo)

---

Recuerda reemplazar los enlaces y las descripciones con la información correcta y actualizada. Este código markdown puede ser colocado directamente en tu archivo README.md en GitHub para presentar tu solución de una manera estructurada y profesional.
