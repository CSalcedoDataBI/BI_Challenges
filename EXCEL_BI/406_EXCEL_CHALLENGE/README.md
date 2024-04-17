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

### Solución de Alejandro Simón usando Power Query 


![Solución Powuer Query](https://github.com/cristobalsalcedo90/BI_Challenges/blob/34526883598d9d8e0b6e4bf600681e037ddcf64e/EXCEL_BI/406_EXCEL_CHALLENGE/files/SolutionAlejandro_Sim%C3%B3n.png)

Copiar Codigo aquí:

```pq
let
  Source = Excel.CurrentWorkbook(){[Name = "Table1"]}[Content],
  Sol = Table.Combine(
    Table.AddColumn(
      Source,
      "A",
      (w) =>
        let
          a = List.Skip(
            List.Generate(
              () => [x = w[Hypotenuse], y = 1],
              each [x] > 0,
              each [x = [x] - 1, y = Number.Sqrt(Number.Power(w[Hypotenuse], 2) - x * x)],
              each [y]
            )
          ),
          b = List.Select(a, each Int64.From(_) = _),
          c = Table.FromRows({{List.Min(b), List.Max(b)}}, {"Base", "Perpendicular"})
        in
          c
    )[A]
  )
in
  Sol


```

### Solución de Ramiro Ayala Chávez



![Solución Power Query](https://github.com/cristobalsalcedo90/BI_Challenges/blob/34526883598d9d8e0b6e4bf600681e037ddcf64e/EXCEL_BI/406_EXCEL_CHALLENGE/files/SolutionRamiro_Ayala_Ch%C3%A1vez.png)

Copiar Codigo aquí:

```pq
let
  S = Excel.CurrentWorkbook(){[Name = "Table1"]}[Content],
  Fx = (A, h) =>
    let
      A = A,
      h = h,
      a = 2 * A,
      b = Number.Power(h * h + 4 * A, 1 / 2),
      c = {1 .. 500},
      d = List.Generate(
        () => [i = 0, j = 1],
        each [i] < List.Count(c),
        each if [j] = List.Count(c) then [i = [i] + 1, j = [i] + 2] else [i = [i], j = [j] + 1],
        each {c{[i]}} & {c{[j] - 1}}
      ),
      e = List.Select(d, each _{0} + _{1} = b and _{0} * _{1} = a){0}
    in
      e,
  f = Table.AddColumn(S, "Base", each Fx([Area], [Hypotenuse]){0}),
  Sol = Table.AddColumn(f, "Perpendicular", each Fx([Area], [Hypotenuse]){1})
in
  Sol
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
