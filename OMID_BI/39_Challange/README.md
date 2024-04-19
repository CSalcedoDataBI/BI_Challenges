# CHALLENGE 39

Este repositorio contiene mis soluciones al Challenge 39, tal como se describe en el reto original proporcionado por Omid Motamedisedeh en su LinkedIn.

## Descripción del Desafío

El desafío requiere:
Descubramos un método ingenioso para abordar el desafío 39: ¡Transformación!
De la lista de productos de la tabla de preguntas, extraiga la lista única de todos los códigos de producto.

![Descripción del desafío](https://github.com/cristobalsalcedo90/BI_Challenges/blob/0a2c380e0018358caae34ba18803c31a67990a05/OMID_BI/39_Challange/Files/Omid.png)

La fuente del desafío puede encontrarse en el perfil de LinkedIn de Omid Motamedisedeh: [
Omid Motamedisedeh](https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7186830879980191745-kfBw?utm_source=share&utm_medium=member_desktop)

## Soluciones

### Solución usando PySpark 🚀 en un Notebook en MicrosoftFabric

Aquí muestro cómo abordé el desafío usando PySpark, destacando el procesamiento distribuido para manejar datos a gran escala.

![Solución PySpark](https://github.com/cristobalsalcedo90/BI_Challenges/blob/0a2c380e0018358caae34ba18803c31a67990a05/OMID_BI/39_Challange/Files/PySpark.PNG)

Copiar Codigo aquí:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, collect_set, array
import pandas as pd

spark = SparkSession.builder.appName("UniqueValuesExtraction").getOrCreate()
file_path = "/lakehouse/default/Files/ChallengeOmid/CH-039 Transformation.xlsx"
pandas_df = pd.read_excel(file_path, usecols=[1, 2, 3, 4], nrows=9)

df = spark.createDataFrame(pandas_df)
df_exploded = df.withColumn("Result - Unique Code", explode(array(*df.columns)))

unique_values = df_exploded.select("Result - Unique Code").na.drop() \
                         .distinct().sort("Result - Unique Code")
unique_values.show()



```
## Detalles de las Funciones Usadas

- **SparkSession**: Esta clase es un punto de entrada a las funcionalidades de Spark SQL. Permite la creación de DataFrames y la ejecución de operaciones SQL, facilitando el procesamiento distribuido de grandes volúmenes de datos. La configuración del entorno de Spark y el manejo de recursos también se gestionan a través de esta sesión.

- **read_excel**: Función de Pandas utilizada para leer un archivo Excel. Permite especificar las columnas a importar y la cantidad de filas a leer, lo que es útil para limitar la carga de datos en memoria cuando se trabaja con archivos grandes o detallados. Al cargar los datos con Pandas, se aprovecha la facilidad de manipulación de datos de Pandas antes de pasar los datos a Spark.

- **createDataFrame**: Este método de `SparkSession` convierte estructuras de datos compatibles, como DataFrames de Pandas, en DataFrames de Spark. Esta conversión es esencial para pasar de la manipulación de datos con Pandas al procesamiento escalable con Spark. Al utilizar este método, se pueden aprovechar las optimizaciones de Spark para el procesamiento distribuido de datos mientras se mantienen las transformaciones iniciales realizadas en Pandas.

- **explode**: Una función de PySpark que se utiliza para transformar cada elemento de una lista en una fila separada, replicando los valores de las otras columnas en cada nueva fila. Esto es especialmente útil para desnormalizar columnas que contienen listas o múltiples valores empaquetados en una sola celda.

- **array**: En PySpark, esta función crea una columna de tipo arreglo a partir de varias columnas del DataFrame. Se utiliza comúnmente en combinación con `explode` para desestructurar arrays y manejar datos a nivel de elemento.

- **distinct**: Método utilizado en DataFrames de PySpark para eliminar filas duplicadas. Es fundamental para asegurar que los análisis o resultados finales no sean sesgados por datos repetidos.

- **sort**: Este método ordena las filas del DataFrame según los valores de una o más columnas. En el contexto de este script, se usa para ordenar los valores únicos extraídos, permitiendo una presentación más organizada y comprensible de los datos.

- **na.drop**: Método para eliminar filas que contienen valores NaN en el DataFrame. Esto ayuda a mantener la calidad de los datos, asegurando que las operaciones y análisis subsiguientes se realicen sobre datos completos y válidos.



### Solución usando Python en un Notebook en MicrosoftFabric

Aquí está mi solución implementada en Python puro, aprovechando las bibliotecas de análisis de datos para una solución eficiente y escalable.

![Solución Python](https://github.com/cristobalsalcedo90/BI_Challenges/blob/0a2c380e0018358caae34ba18803c31a67990a05/OMID_BI/39_Challange/Files/Python.png)

Copiar Codigo aquí:
```python
import pandas as pd
file_path = "/lakehouse/default/Files/ChallengeOmid/CH-039 Transformation.xlsx"
df = pd.read_excel(file_path, usecols=[1, 2, 3, 4], nrows=9)
df_melted = df.melt(var_name='Attribute', value_name='Result - Unique Code')
unique_values = pd.Series(df_melted['Result - Unique Code'].dropna() \
                .unique()).sort_values().tolist()
result_df = pd.DataFrame({"Result - Unique Code": unique_values})
print(result_df)
```
# Extracción y Ordenamiento de Valores Únicos en Python

Este script utiliza Python y Pandas para leer datos desde un archivo Excel, transformar estos datos de un formato ancho a uno largo, y extraer y ordenar valores únicos de ciertas columnas. El objetivo es simplificar la manipulación de datos y facilitar análisis posteriores o integraciones.

## Cómo Funciona

1. **Leer Datos**: El script comienza leyendo un archivo Excel especificado, seleccionando ciertas columnas y un número limitado de filas.
2. **Transformar Datos**: Utiliza la función `melt` de Pandas para transformar el DataFrame de un formato ancho a uno más largo.
3. **Extracción de Valores Únicos**: A partir de los datos transformados, se extraen valores únicos, excluyendo cualquier dato faltante (NaN).
4. **Ordenamiento y Visualización**: Los valores únicos son ordenados y convertidos en un nuevo DataFrame para su fácil visualización.



### Solución Power Query


Aquí está mi solución implementada en Power Query.

![Solución Power Query](https://github.com/cristobalsalcedo90/BI_Challenges/blob/9ed693393f32c097d5445725480cf6e356f9111b/OMID_BI/39_Challange/Files/PowerQuery.PNG)

```pq
let
  Source = Excel.CurrentWorkbook(){[Name = "Table2"]}[Content], 
  #"Unpivoted Other Columns" = Table.FromList(
    List.Sort(List.Distinct(Table.UnpivotOtherColumns(Source, {}, "Attribute", "Value")[Value])), 
    null, 
    {"Result - Unique Code"}
  )
in
  #"Unpivoted Other Columns"

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
