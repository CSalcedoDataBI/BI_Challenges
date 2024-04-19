# 428_EXCEL_CHALLENGE

Este repositorio contiene mis soluciones al 428 Excel Challenge, tal como se describe en el reto original proporcionado por Excel BI en su LinkedIn.

## Descripción del Desafío

El desafío requiere:
Tuvimos un desafío sobre el valor de la resistencia: <https://lnkd.in/dqE24cez>
Ahora, expresemos los valores derivados como K, M o G (Kilo, Mega o Giga).

Para las bandas de color dadas en la Columna E, calcule la resistencia total.
Las bandas de color tienen códigos de color indicados en la columna B. Se les asignan valores de 0 a 9 secuencialmente.
RedOrangeGreen se escribe como reorgr en códigos de color.
El último código de color es para el número de veces que aparecerán los ceros.
Ej. reorgr = re & o & gr = 2 & 3 & (5 veces 0s) = 2300000
bugyvibl = bu & gy & vi & bl = 6 & 8 & 7 & (0 veces 0s) = 687

Los valores deben expresarse en K (Kilo) / M (Mega) / G (Giga) Ohm o sin estos solo en Ohm. Al menos un dígito o como máximo 3 dígitos deben estar en el lado izquierdo del decimal si se puede expresar en K / M / G. Básicamente, esto equivale a mil, millones y miles de millones de formato de monedas.

123 = 123 ohmios
1234 = 1.234 K Ohm
12345 = 12.345 K Ohm
123456 = 123.456 K Ohm
1234567 = 1.234567 M Ohm
1234567893 = 1,234567893 G Ohm

![Descripción del desafío](https://github.com/cristobalsalcedo90/BI_Challenges/blob/72d089bb741fb3b3f5bbbded10d57f013b0fafa6/428_EXCEL_CHALLENGE/Files/ExcelBi.png)

La fuente del desafío puede encontrarse en el perfil de LinkedIn de Excel BI: [Excel BI LinkedIn Post](https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7186936560318111744-ys1D?utm_source=share&utm_medium=member_desktop)

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

file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_438 - Resistor Value_v2.xlsx"

panda_df = pd.read_excel(file_path, usecols=[0, 1, 2, 4, 5])

color_code_dict = panda_df.set_index('Code')['Value'].to_dict()

def calculate_resistance(color_band):
    if pd.isnull(color_band):
        return None
    
    color_codes = color_band[:-2]
    multiplier_code = color_band[-2:]
    
    numeric_value = ''
    for i in range(0, len(color_codes), 2):
        color_code = color_codes[i:i+2]
        if color_code in color_code_dict:
            numeric_value += str(color_code_dict[color_code])
        else:
            return 'Invalid Color Code'
    
    if multiplier_code in color_code_dict:
        multiplier_value = color_code_dict[multiplier_code]
    else:
        return 'Invalid Multiplier Code'
    
    resistance_value = int(numeric_value) * (10 ** multiplier_value)
    
    return format_resistance(resistance_value, multiplier_value)

def format_resistance(value, multiplier):
    if value >= 1e9:
        formatted_value = f"{value / 1e9} G Ohm"
    elif value >= 1e6:
        formatted_value = f"{value / 1e6} M Ohm"
    elif value >= 1e3:
        formatted_value = f"{value / 1e3} K Ohm"
    else:
        formatted_value = f"{value} Ohm"
    
    formatted_value = formatted_value.rstrip('0').rstrip('.') if '.' in formatted_value else formatted_value
    return formatted_value

panda_df['MySolution'] = panda_df['Color Bands'].apply(calculate_resistance)

print(panda_df[['Answer Expected', 'MySolution']])


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
