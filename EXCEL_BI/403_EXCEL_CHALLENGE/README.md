# 403_EXCEL_CHALLENGE

Este repositorio contiene mis soluciones al 403 Excel Challenge, tal como se describe en el reto original proporcionado por Excel BI en su LinkedIn.

## Descripción del Desafío

El desafío requiere:
Genere la suma del valor y el % del valor para los tramos de años de 5 años cada uno.

(No es necesario que su fórmula sea una sola fórmula. Puede escribir varias fórmulas para llegar a una solución. Además, su fórmula no tiene por qué ser diferente de las demás, siempre y cuando haya elaborado su fórmula de forma independiente)

![Descripción del desafío](https://github.com/cristobalsalcedo90/BI_Challenges/blob/72d089bb741fb3b3f5bbbded10d57f013b0fafa6/428_EXCEL_CHALLENGE/Files/ExcelBi.png)

La fuente del desafío puede encontrarse en el perfil de LinkedIn de Excel BI: [Excel BI LinkedIn Post](https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7169179556946329600-4n_0?utm_source=share&utm_medium=member_desktop)

## Soluciones

### Solución usando PySpark 🚀 en un Notebook en MicrosoftFabric

Aquí muestro cómo abordé el desafío usando PySpark, destacando el procesamiento distribuido para manejar datos a gran escala.

![Solución PySpark](https://github.com/cristobalsalcedo90/BI_Challenges/blob/72d089bb741fb3b3f5bbbded10d57f013b0fafa6/428_EXCEL_CHALLENGE/Files/428_EXCEL_CHALLENGE_PySpark.png)

Copiar Codigo aquí:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import BooleanType
from datetime import datetime
spark = SparkSession.builder.appName("CHALLENGE428").getOrCreate()
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_428 - Chinese National ID.xlsx"
pandas_df = pd.read_excel(file_path, usecols=[0], nrows=10)
spark_df = spark.createDataFrame(pandas_df)
general_pattern = "\\d{6}\\d{8}\\d{3}[0-9X]"
def is_valid_date(ID):
    date_str = ID[6:14]
    try:
        datetime.strptime(date_str, "%Y%m%d")
        return True
    except ValueError:
        return False
def is_ID_valid(ID):
    base = [int(digit) for digit in ID[:17]]
    I = list(range(18, 1, -1))
    WI = [2**(i-1) % 11 for i in I]
    S = sum(digit * weight for digit, weight in zip(base, WI))
    C = (12 - (S % 11)) % 11
    C = 'X' if C == 10 else str(C)

    whole_id = ''.join(map(str, base)) + C
    return whole_id == ID
is_valid_date_udf = udf(is_valid_date, BooleanType())
is_ID_valid_udf = udf(is_ID_valid, BooleanType())
filtered_data = spark_df.filter(col("National ID").rlike(general_pattern)) \
                        .withColumn("Is Valid Date", is_valid_date_udf(col("National ID"))) \
                        .withColumn("Is ID Valid", is_ID_valid_udf(col("National ID"))) \
                        .filter(col("Is Valid Date") & col("Is ID Valid")) \
                        .drop("Is Valid Date", "Is ID Valid") \
                        .withColumnRenamed("National ID", "My Solution")
filtered_data.show()


```

### Solución usando Python en un Notebook en MicrosoftFabric

Aquí está mi solución implementada en Python puro, aprovechando las bibliotecas de análisis de datos para una solución eficiente y escalable.

![Solución Python](https://github.com/cristobalsalcedo90/BI_Challenges/blob/72d089bb741fb3b3f5bbbded10d57f013b0fafa6/428_EXCEL_CHALLENGE/Files/428_EXCEL_CHALLENGE_Python.png)

Copiar Codigo aquí:

```python
import pandas as pd
from datetime import datetime

file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_428 - Chinese National ID.xlsx"
pandas_df = pd.read_excel(file_path, usecols=[0], nrows=10)

general_pattern = "\\d{6}\\d{8}\\d{3}[0-9X]"

def is_valid_date(ID):
    date_str = ID[6:14]
    try:
        datetime.strptime(date_str, "%Y%m%d")
        return True
    except ValueError:
        return False

def is_ID_valid(ID):
    base = [int(digit) for digit in ID[:17]]
    I = list(range(18, 1, -1))
    WI = [2**(i-1) % 11 for i in I]
    S = sum(digit * weight for digit, weight in zip(base, WI))
    C = (12 - (S % 11)) % 11
    C = 'X' if C == 10 else str(C)

    whole_id = ''.join(map(str, base)) + C
    return whole_id == ID
filtered_data = pandas_df[pandas_df['National ID'].str.match(general_pattern).fillna(False)].copy()
filtered_data['My Solution'] = filtered_data['National ID'].apply(lambda x: x if is_valid_date(x) and is_ID_valid(x) else pd.NA)

filtered_data.drop(columns=['National ID'], inplace=True)
filtered_data = filtered_data.dropna(subset=['My Solution'])
print(filtered_data)

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
