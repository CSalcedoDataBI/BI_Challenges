#https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7173890586880458752-rEx5?utm_source=share&utm_medium=member_desktop
import pandas as pd

# Definir la ruta al archivo Excel.
excel_file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_412 - Square Sum Iterate till a Single Digit .xlsx"

# Cargar el archivo Excel en un DataFrame de Pandas.
pandas_df = pd.read_excel(excel_file_path, usecols=[0], header=1)

# Definir una función para calcular el dígito final y el número de iteraciones.
# Ajustada para manejar números de un solo dígito desde el inicio.
def calculate_final_digit_and_iterations(number):
    iterations = 0
    # Procesar el número al menos una vez si es de un solo dígito.
    number = sum(int(digit) ** 2 for digit in str(number))
    if number < 10:
        return pd.Series([number, 1])  # Retorna después de una iteración si ya es un dígito único.
    while number >= 10:
        number = sum(int(digit) ** 2 for digit in str(number))
        iterations += 1
    return pd.Series([number, iterations + 1])  # +1 para contar la primera iteración para dígitos únicos.

# Aplicar la función a cada número en la columna del DataFrame y crear dos nuevas columnas.
pandas_df[['Final Single Digit', 'Number of Iterations']] = pandas_df.apply(
    lambda row: calculate_final_digit_and_iterations(row.iloc[0]), axis=1)

# Mostrar el DataFrame procesado.
print(pandas_df)
