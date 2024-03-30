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
## Otras Soluciones

### Solución en Power Query presentada por Aditya Kumar Darak

Me gustaría destacar una solución alternativa presentada por Aditya Kumar Darak, que utiliza Power Query en Excel para abordar el desafío.

Para más detalles sobre esta solución, puedes visitar la discusión original en LinkedIn aquí: [Ver Solución de Aditya Kumar Darak](https://www.linkedin.com/feed/update/urn:li:activity:7179326423331921920?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7179326423331921920%2C7179332333995450368%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287179332333995450368%2Curn%3Ali%3Aactivity%3A7179326423331921920%29).

### Implementación de la Solución en Power Query 1🛠️
```powerquery
let
  Source = Excel.CurrentWorkbook(){[Name = "Data"]}[Content], 
  Series = {{"A" .. "Z"}, {"a" .. "z"}, {"0" .. "9"}}, 
  Result = Table.AddColumn(
    Source, 
    "Answer", 
    each [
      a = (x, y, z) => Text.Combine(Splitter.SplitTextByCharacterTransition(x, y)(z), ", "), 
      b = a(Series{0}, Series{1} & Series{2}, [Data]), 
      c = a(Series{1}, Series{0} & Series{2}, b), 
      d = a(Series{2}, Series{0} & Series{1}, c)
    ][d]
  )
in
  Result
```
### Solución en Power Query presentada por Luan Rodrigues
Para más detalles sobre esta solución, puedes visitar la discusión original en LinkedIn aquí: [Ver Solución de Luan Rodrigues](https://www.linkedin.com/feed/update/urn:li:activity:7179326423331921920?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7179326423331921920%2C7179570378703310848%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287179570378703310848%2Curn%3Ali%3Aactivity%3A7179326423331921920%29).

### Implementación de la Solución en Power Query 2 🛠️
```powerquery
let
  Fonte = Excel.CurrentWorkbook(){[Name="Data"]}[Content], 
  res = Table.AddColumn(
    Fonte, 
    "Personalizar", 
    each Text.Combine(
      List.Combine(
        List.TransformMany(
          {{"0" .. "9"}, {"A" .. "z"}}, 
          (x) =>
            let
              a = Text.Split(
                Text.Combine(List.Transform(Text.ToList([Data]), each Text.Select(_, x)), ", "), 
                ", , "
              ), 
              b = List.Transform(a, each Text.Remove(_, {",", " "})), 
              c = List.Select(b, each _ <> "")
            in
              c, 
          (x, y) =>
            List.TransformMany(
              Splitter.SplitTextByCharacterTransition({"A" .. "Z"}, {"a" .. "z"})(y), 
              (a) => Splitter.SplitTextByCharacterTransition({"a" .. "z"}, {"A" .. "Z"})(a), 
              (o, p) => p
            )
        )
      ), 
      ", "
    )
  )
in
    res
```
### Solución en Power Query presentada por Luan Rodrigues
Para más detalles sobre esta solución, puedes visitar la discusión original en LinkedIn aquí: [Ver Solución de Venkata Rajesh](https://www.linkedin.com/feed/update/urn:li:activity:7179326423331921920?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7179326423331921920%2C7179420495744827393%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287179420495744827393%2Curn%3Ali%3Aactivity%3A7179326423331921920%29).

### Implementación de la Solución en Power Query 3 🛠️
```powerquery
let
  Source = Excel.CurrentWorkbook(){[Name="Data"]}[Content], 
  Output = Table.AddColumn(
    Source, 
    "Expected", 
    each [
      x = Text.ToList([Data]), 
      y = (x as text) =>
        if List.Contains({"0" .. "9"}, x) then
          "number"
        else if List.Contains({"a" .. "z"}, x) then
          "lower"
        else
          "upper", 
      z = List.Accumulate(
        {0 .. List.Count(x) - 2}, 
        "", 
        (state, current) =>
          if y(x{current}) = y(x{current + 1}) then
            state & x{current}
          else
            state & x{current} & " ,"
      )
        & List.Last(x)
    ][z]
  )
in
    Output
```
## Agradecimientos y Referencias
Me gustaría agradecer a [Aditya Kumar Darak](https://www.linkedin.com/feed/update/urn:li:activity:7179326423331921920?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7179326423331921920%2C7179332333995450368%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287179332333995450368%2Curn%3Ali%3Aactivity%3A7179326423331921920%29), [Luan Rodrigues](https://www.linkedin.com/feed/update/urn:li:activity:7179326423331921920?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7179326423331921920%2C7179570378703310848%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287179570378703310848%2Curn%3Ali%3Aactivity%3A7179326423331921920%29) y [Venkata Rajesh](https://www.linkedin.com/feed/update/urn:li:activity:7179326423331921920?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7179326423331921920%2C7179420495744827393%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287179420495744827393%2Curn%3Ali%3Aactivity%3A7179326423331921920%29) por compartir esta ingeniosa solución de Power Query en LinkedIn. Su contribución proporciona una perspectiva valiosa y un método alternativo para abordar el desafío.

Un agradecimiento especial a la comunidad de [Excel BI](https://www.linkedin.com/in/excelbi/) por proporcionar estos desafiantes y enriquecedores problemas que nos permiten crecer profesionalmente en el campo del BI.

## ¿Cómo utilizar este repositorio?

Puede clonar este repositorio y ejecutar los notebooks proporcionados para ver cómo se implementaron las soluciones. Se proporcionan instrucciones detalladas dentro de cada notebook.

## Contacto

Si tienes alguna pregunta o deseas conectarte, no dudes en visitar mi perfil de LinkedIn.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Cristobal%20Salcedo-blue)](https://www.linkedin.com/in/cristobal-salcedo)

---

Recuerda reemplazar los enlaces y las descripciones con la información correcta y actualizada. Este código markdown puede ser colocado directamente en tu archivo README.md en GitHub para presentar tu solución de una manera estructurada y profesional.
