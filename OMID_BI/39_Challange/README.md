# CHALLENGE 39

Este repositorio contiene mis soluciones al Challenge 39, tal como se describe en el reto original proporcionado por Omid Motamedisedeh en su LinkedIn.

## Descripción del Desafío

El desafío requiere:
Descubramos un método ingenioso para abordar el desafío 39: ¡Transformación!
De la lista de productos de la tabla de preguntas, extraiga la lista única de todos los códigos de producto.

![Descripción del desafío](https://github.com/cristobalsalcedo90/BI_Challenges/blob/6a18a1209d84d96b7c7a63d0a7ed346a3a3ceb50/OMID_BI/36_Challenge/files/Challenge.png)

La fuente del desafío puede encontrarse en el perfil de LinkedIn de Omid Motamedisedeh: [
Omid Motamedisedeh](https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7186830879980191745-kfBw?utm_source=share&utm_medium=member_desktop)

## Soluciones

### Solución usando PySpark 🚀 en un Notebook en MicrosoftFabric

Aquí muestro cómo abordé el desafío usando PySpark, destacando el procesamiento distribuido para manejar datos a gran escala.

![Solución PySpark](https://github.com/cristobalsalcedo90/BI_Challenges/blob/4a110c7ca86b8757e730e703e0c9e1d8f6e6b4dc/EXCEL_BI/403_EXCEL_CHALLENGE/files/403_EXCEL_CHALLENGE.PNG)

Copiar Codigo aquí:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, collect_set, array
import pandas as pd

spark = SparkSession.builder.appName("UniqueValuesExtraction").getOrCreate()
file_path = "/lakehouse/default/Files/ChallengeOmid/CH-039 Transformation.xlsx"
pandas_df = pd.read_excel(file_path, usecols=[1, 2, 3, 4], nrows=8)

df = spark.createDataFrame(pandas_df)
df_exploded = df.withColumn("Result - Unique Code", explode(array(*df.columns)))

unique_values = df_exploded.select("Result - Unique Code").na.drop() \
                         .distinct().sort("Result - Unique Code")
unique_values.show()



```
### Solución usando Python en un Notebook en MicrosoftFabric

Aquí está mi solución implementada en Python puro, aprovechando las bibliotecas de análisis de datos para una solución eficiente y escalable.

![Solución Python](https://github.com/cristobalsalcedo90/BI_Challenges/blob/e2c941df816763045366df0658358ab82f4168ea/427_EXCEL_CHALLENGE/Files/427_EXCEL_CHALLENGE_Python.png)

Copiar Codigo aquí:
```python
import pandas as pd
file_path = "/lakehouse/default/Files/ChallengeOmid/CH-039 Transformation.xlsx"
df = pd.read_excel(file_path, usecols=[1, 2, 3, 4], nrows=8)
df_melted = df.melt(var_name='Attribute', value_name='Result - Unique Code')
unique_values = pd.Series(df_melted['Result - Unique Code'].dropna() \
                .unique()).sort_values().tolist()
result_df = pd.DataFrame({"Result - Unique Code": unique_values})
print(result_df)
```



## Agradecimientos y Referencias

Un agradecimiento especial a la comunidad de [Omid Motamedisedeh](https://www.linkedin.com/in/omid-motamedisedeh-74aba166/) por proporcionar estos desafiantes y enriquecedores problemas que nos permiten crecer profesionalmente en el campo del BI.

## ¿Cómo utilizar este repositorio?

Puede clonar este repositorio y ejecutar los notebooks proporcionados para ver cómo se implementaron las soluciones. Se proporcionan instrucciones detalladas dentro de cada notebook.

## Contacto

Si tienes alguna pregunta o deseas conectarte, no dudes en visitar mi perfil de LinkedIn.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Cristobal%20Salcedo-blue)](https://www.linkedin.com/in/cristobal-salcedo)

---

Recuerda reemplazar los enlaces y las descripciones con la información correcta y actualizada. Este código markdown puede ser colocado directamente en tu archivo README.md en GitHub para presentar tu solución de una manera estructurada y profesional.
