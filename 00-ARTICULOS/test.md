### Power Query: Transformación de Texto

La solución inicial para el desafío se implementó en Power Query, una herramienta poderosa para la transformación de datos dentro de Excel. Este enfoque permite manipular y preparar datos para análisis de una manera eficiente y escalable, incluso para usuarios sin profundos conocimientos de programación.

#### Descripción del Código

El script en Power Query realiza las siguientes operaciones paso a paso:

```powerquery
let
  Source = Excel.CurrentWorkbook(){0}[Content], 
  AddCustomColumn = Table.AddColumn(
    Source, 
    "ExpectedAnswer", 
    each 
      let
        TextToProcess = [Data], 
        SplitText = Splitter.SplitTextByCharacterTransition({"A" .. "z"}, {"0" .. "9"})(
          TextToProcess
        ), 
        TransformedText = List.Accumulate(
          SplitText, 
          "", 
          (state, current) =>
            state
              & ", "
              & Text.Combine(
                Splitter.SplitTextByCharacterTransition({"0" .. "9"}, {"A" .. "z"})(current), 
                ", "
              )
        )
      in
        if Text.Length(TransformedText) > 2 then Text.Middle(TransformedText, 2) else ""
  )
in
  AddCustomColumn
```

### Explicación Paso a Paso

- **Carga de Datos**: `Source = Excel.CurrentWorkbook(){0}[Content]` carga la primera tabla encontrada en el libro de trabajo actual. Este es el punto de partida para la transformación.

- **Añadir Columna Personalizada**: `Table.AddColumn` se utiliza para añadir una nueva columna al conjunto de datos, denominada "ExpectedAnswer". Esta columna contendrá el resultado de las transformaciones aplicadas a cada fila de la columna "Data".

#### Transformación de Cada Fila:

  - **Extracción de Texto**: Se asigna el valor de la columna "Data" a la variable `TextToProcess`.
  
  - **División de Texto por Transición de Carácter**: `Splitter.SplitTextByCharacterTransition` divide el texto en fragmentos cada vez que encuentra una transición de letras a números o viceversa.
  
  - **Acumulación y Combinación de Fragmentos**: `List.Accumulate` se utiliza para iterar sobre cada fragmento de texto, combinándolos en un solo string, donde cada fragmento está separado por comas. Dentro de este proceso, se vuelve a dividir y combinar cada fragmento para asegurar la correcta inserción de comas.

- **Limpieza del Resultado Final**: El resultado de `List.Accumulate` puede comenzar con una coma y un espacio debido a cómo se construye la acumulación. Se utiliza `Text.Middle` para extraer el texto resultante sin estos caracteres iniciales, si están presentes.

### Resultado

Este proceso convierte cadenas de texto que intercalan letras y números en una lista separada por comas de elementos alfabéticos y numéricos. Por ejemplo, "a1b2" se transformaría en "a, 1, b, 2".

Este enfoque en Power Query ofrece una solución robusta y flexible para la preparación de datos, permitiendo manipulaciones complejas de texto con un control detallado sobre cada paso del proceso de transformación.



## ¿Cómo utilizar este repositorio?

Puede clonar este repositorio y ejecutar los notebooks proporcionados para ver cómo se implementaron las soluciones. Se proporcionan instrucciones detalladas dentro de cada notebook.

## Contacto

Si tienes alguna pregunta o deseas conectarte, no dudes en visitar mi perfil de LinkedIn.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Cristobal%20Salcedo-blue)](https://www.linkedin.com/in/cristobal-salcedo)

---

Recuerda reemplazar los enlaces y las descripciones con la información correcta y actualizada. Este código markdown puede ser colocado directamente en tu archivo README.md en GitHub para presentar tu solución de una manera estructurada y profesional.