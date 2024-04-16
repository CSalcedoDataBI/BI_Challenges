# CHALLENGE 36

Este repositorio contiene mis soluciones al Challenge 36, tal como se describe en el reto original proporcionado por Omid Motamedisedeh en su LinkedIn.

## Descripción del Desafío

El desafío requiere:
Descubramos un método ingenioso para abordar el reto 36: En los modelos multiobjetivo, en lugar de una única solución, nos encontramos con un frente de Pareto que incluye todas las soluciones no dominantes, y en esta cuestión queremos extraer todas las soluciones no dominantes.

Una solución, digamos 'a', se considera no dominante si no hay otra solución, como 'b', donde todos los valores objetivos de 'b' son mayores que los de 'a'.
Por ejemplo, el identificador de solución 1, dominado por los identificadores de solución 7, 8, 9 y 11, se excluye de la tabla de resultados.

![Descripción del desafío](https://github.com/cristobalsalcedo90/BI_Challenges/blob/6a18a1209d84d96b7c7a63d0a7ed346a3a3ceb50/OMID_BI/36_Challenge/files/Challenge.png)

La fuente del desafío puede encontrarse en el perfil de LinkedIn de Excel BI: [Excel LinkedIn Post](https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7184656532284882944-UuQm?utm_source=share&utm_medium=member_desktop)

## Soluciones

### Solución usando Python en un Notebook en MicrosoftFabric

Aquí está mi solución implementada en Python puro, aprovechando las bibliotecas de análisis de datos para una solución eficiente y escalable.

![Solución Python](https://github.com/cristobalsalcedo90/BI_Challenges/blob/3304ad4a782789036b8365c58ed166fbecd40a92/OMID_BI/36_Challenge/files/36_CHALLENGE_Python.png)

Copiar Codigo aquí:

```python
import pandas as pd

path_file = "/lakehouse/default/Files/ChallengeOmid/CH-036 Pareto Line.xlsx"

pandas_df = pd.read_excel(path_file, header=1, usecols=[1, 2, 3, 4])
result = pandas_df.apply(
    lambda row: not any((pandas_df.iloc[:, 1:4] > row[1:4]).all(axis=1)), axis=1
)
result = pandas_df.apply(
    lambda row: not any((pandas_df.iloc[:, 1:4] > row[1:4]).all(axis=1)), axis=1
)
result = (
    result[result].index.to_frame(index=False).rename(columns={0: "Solution ID"}) + 1
)
result["Solution ID"] = result["Solution ID"].astype(int)
print(result)


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
