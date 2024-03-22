# 418_EXCEL_CHALLENGE

Este repositorio contiene mis soluciones al 418 Excel Challenge, tal como se describe en el reto original proporcionado por Excel BI en su LinkedIn.

## Descripción del Desafío

El desafío requiere:
Pivote la tabla dada para las combinaciones de Fecha / ID de Emp con Hora mínima y máxima. La hora mínima y la hora máxima aparecerán en filas alternas. Primero aparecerá el tiempo mínimo y luego el tiempo máximo en la otra fila.

![Descripción del desafío](https://github.com/cristobalsalcedo90/BI_Challenges/blob/c9961e9a15f3befbee69580e10b67febac26e815/418_EXCEL_CHALLENGE/Files/ExcelBi.png)

La fuente del desafío puede encontrarse en el perfil de LinkedIn de Excel BI: [Excel BI LinkedIn Post](https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7176789688647573505-0c2a?utm_source=share&utm_medium=member_desktop)

## Soluciones

### Solución usando PySpark en un Notebook en MicrosoftFabric

Aquí muestro cómo abordé el desafío usando PySpark, destacando el procesamiento distribuido para manejar datos a gran escala.

![Solución PySpark](https://github.com/cristobalsalcedo90/BI_Challenges/blob/c9961e9a15f3befbee69580e10b67febac26e815/418_EXCEL_CHALLENGE/Files/418_EXCEL_CHALLENGE_PySpark.png)

Codigo:
```
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

```

### Solución usando Python en un Notebook en MicrosoftFabric

Aquí está mi solución implementada en Python puro, aprovechando las bibliotecas de análisis de datos para una solución eficiente y escalable.

![Solución Python](https://github.com/cristobalsalcedo90/BI_Challenges/blob/c9961e9a15f3befbee69580e10b67febac26e815/418_EXCEL_CHALLENGE/Files/418_EXCEL_CHALLENGE_Python.png)

## ¿Cómo utilizar este repositorio?

Puede clonar este repositorio y ejecutar los notebooks proporcionados para ver cómo se implementaron las soluciones. Se proporcionan instrucciones detalladas dentro de cada notebook.

## Contacto

Si tienes alguna pregunta o deseas conectarte, no dudes en visitar mi perfil de LinkedIn.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Cristobal%20Salcedo-blue)](https://www.linkedin.com/in/cristobal-salcedo)

---

Recuerda reemplazar los enlaces y las descripciones con la información correcta y actualizada. Este código markdown puede ser colocado directamente en tu archivo README.md en GitHub para presentar tu solución de una manera estructurada y profesional.
