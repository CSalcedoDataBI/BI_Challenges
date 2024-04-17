# 406_EXCEL_CHALLENGE

Este repositorio contiene mis soluciones al 406 Excel Challenge, que consiste en generar una secuencia numérica siguiendo una estructura de contorno específica, tal como se describe en el reto original proporcionado por Excel BI en su LinkedIn.

## Descripción del Desafío

Para un triángulo rectángulo, se dan el área y la hipotenusa. Halla la base y las perpendiculares para conjuntos dados de área e hipotenusa. 
Hipotenusa^2 = Base^2 + Perpendicular^2
Área = (Base * Perpendicular)/2 
Nota: he asumido que la base es un lado más pequeño y la perpendicular es un lado más grande. No es necesario hacer esta suposición. 

(No es necesario que su fórmula sea una sola fórmula. Puede escribir varias fórmulas para llegar a una solución. Además, su fórmula no tiene por qué ser diferente de las demás, siempre y cuando haya elaborado su fórmula de forma independiente)

![Descripción del desafío](https://github.com/cristobalsalcedo90/BI_Challenges/blob/f938e0bb67175a39b0e61a60fb4707671a653466/EXCEL_BI/407_EXCEL_CHALLENGE/files/Excel_BI.png)

La fuente del desafío puede encontrarse en el perfil de LinkedIn de Excel BI: [Excel BI LinkedIn Post](https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7170991492973355008-xiaI?utm_source=share&utm_medium=member_desktop)

## Soluciones

### Solución usando PySpark 🚀 en un Notebook en MicrosoftFabric

Aquí muestro cómo abordé el desafío usando PySpark, destacando el procesamiento distribuido para manejar datos a gran escala.

![Solución PySpark](https://github.com/cristobalsalcedo90/BI_Challenges/blob/f938e0bb67175a39b0e61a60fb4707671a653466/EXCEL_BI/407_EXCEL_CHALLENGE/files/EXCEL_CHALLENGE_407_PySpark.PNG)

Copiar Codigo aquí:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType
import pandas as pd
spark = SparkSession.builder.appName("Excel to Spark DF").getOrCreate()
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_407 - Mirror Cipher.xlsx"

pandas_df = pd.read_excel(file_path, usecols="A:B")
spark_df = spark.createDataFrame(pandas_df)

def mirror_cipher_caesar_shift(plaintext, shift):
    words_reversed = plaintext.split()[::-1]
    mirrored_sentence = ' '.join(word[::-1] for word in words_reversed)
    encrypted_sentence = ''.join(
        chr(((ord(char) - 65 + shift) % 26) + 65) if char.isupper() else
        chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else char
        for char in mirrored_sentence
    )
    return encrypted_sentence
    
encrypt_udf = udf(mirror_cipher_caesar_shift, StringType())
df_result = spark_df.withColumn("Answer Expected", encrypt_udf(col("Plain Text"), col("Shift")))
display(df_result)


```

### Solución usando Python en un Notebook en MicrosoftFabric

Aquí está mi solución implementada en Python puro, aprovechando las bibliotecas de análisis de datos para una solución eficiente y escalable.

![Solución Python](https://github.com/cristobalsalcedo90/BI_Challenges/blob/f938e0bb67175a39b0e61a60fb4707671a653466/EXCEL_BI/407_EXCEL_CHALLENGE/files/EXCEL_CHALLENGE_407_Python.PNG)

Copiar Codigo aquí:

```python
import pandas as pd

# Path to the Excel file to be read
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_407 - Mirror Cipher.xlsx"

# Load the Excel file into a Pandas DataFrame, using only columns "A" and "B"
df = pd.read_excel(file_path, usecols="A:B")

# Definition of the encryption function
def mirror_cipher_caesar_shift(plaintext, shift):
    """
    This function applies a mirror cipher followed by a Caesar cipher.
    
    - First, it reverses the order of the words and then reverses the letters within each word.
    - Then it applies a Caesar shift with the given value.
    
    Parameters:
    - plaintext: The original text to be encrypted.
    - shift: Shift value for the Caesar cipher.
    
    Returns:
    - Encrypted text applying the mirror cipher first and then the Caesar cipher.
    """
    # Reverse the order of the words
    words_reversed = plaintext.split()[::-1]
    # Reverse the letters within each word
    mirrored_sentence = ' '.join(word[::-1] for word in words_reversed)
    # Apply the Caesar cipher
    encrypted_sentence = ''.join(
        chr(((ord(char) - 65 + shift) % 26) + 65) if char.isupper() else
        chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else char
        for char in mirrored_sentence
    )
    return encrypted_sentence

# Apply the encryption function to each row of the DataFrame
df['Encrypted'] = df.apply(lambda row: mirror_cipher_caesar_shift(row['Plain Text'], row['Shift']), axis=1)

# Display the DataFrame with the results
print(df)

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
