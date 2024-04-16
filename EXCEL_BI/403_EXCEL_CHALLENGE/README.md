# 403_EXCEL_CHALLENGE

Este repositorio contiene mis soluciones al 403 Excel Challenge, tal como se describe en el reto original proporcionado por Excel BI en su LinkedIn.

## Descripción del Desafío

El desafío requiere:
Genere la suma del valor y el % del valor para los tramos de años de 5 años cada uno.

(No es necesario que su fórmula sea una sola fórmula. Puede escribir varias fórmulas para llegar a una solución. Además, su fórmula no tiene por qué ser diferente de las demás, siempre y cuando haya elaborado su fórmula de forma independiente)

![Descripción del desafío](https://github.com/cristobalsalcedo90/BI_Challenges/blob/4a110c7ca86b8757e730e703e0c9e1d8f6e6b4dc/EXCEL_BI/403_EXCEL_CHALLENGE/files/Excel_BI.png)

La fuente del desafío puede encontrarse en el perfil de LinkedIn de Excel BI: [Excel BI LinkedIn Post](https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7169179556946329600-4n_0?utm_source=share&utm_medium=member_desktop)

## Soluciones

### Solución usando PySpark 🚀 en un Notebook en MicrosoftFabric

Aquí muestro cómo abordé el desafío usando PySpark, destacando el procesamiento distribuido para manejar datos a gran escala.

![Solución PySpark](https://github.com/cristobalsalcedo90/BI_Challenges/blob/4a110c7ca86b8757e730e703e0c9e1d8f6e6b4dc/EXCEL_BI/403_EXCEL_CHALLENGE/files/403_EXCEL_CHALLENGE.PNG)

Copiar Codigo aquí:

```python
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7169179556946329600-4n_0/
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat, lit, sum as _sum, round, asc
import pandas as pd

# Path to the Excel file
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_403 - Generate Pivot Table.xlsx"
sheet_name = "Sheet1"
# Read data from Excel with Pandas
df_pandas = pd.read_excel(file_path, sheet_name=sheet_name, usecols="A:B", nrows=100)

# Start SparkSession
spark = SparkSession.builder.appName("GroupByInterval").getOrCreate()

# Convert to PySpark DataFrame
df_spark = spark.createDataFrame(df_pandas)

# Display the original DataFrame (optional)
df_spark.show(3)

# Base year for the group calculation
base_year = 1990

# Group by 5-year intervals
df_grouped = df_spark.withColumn("YearGroup", ((col("Year") - base_year) / 5).cast("int") * 5 + base_year) \
    .groupBy("YearGroup") \
    .agg(_sum("Value").alias("Sum of Value"))

# Calculate the total of all values for later percentage calculation
total_value = df_grouped.agg(_sum("Sum of Value").alias("total")).first()["total"]

# Calculate the percentage for each group and convert to integer
df_grouped = df_grouped.withColumn("% of Value", 
                                   round((col("Sum of Value") / total_value) * 100).cast("int"))

# Add the year interval labels
df_grouped = df_grouped.withColumn("Year", concat(col("YearGroup"), lit("-"), col("YearGroup") + 4)) \
    .selectExpr("Year", "`Sum of Value`", "`% of Value` || '%' as `% of Value`")

# Ensure the year groups are sorted
df_grouped = df_grouped.orderBy(asc("YearGroup"))

# Add the grand total at the end
df_grand_total = spark.createDataFrame([("Grand Total", total_value, "100%")], ["Year", "Sum of Value", "% of Value"])
df_final = df_grouped.unionByName(df_grand_total)

# Display the final result
df_final.show()


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
