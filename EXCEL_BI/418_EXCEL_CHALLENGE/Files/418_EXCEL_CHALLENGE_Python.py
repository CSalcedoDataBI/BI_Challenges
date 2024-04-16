import pandas as pd

# Cargar los datos
file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_418 - Pivot on Min and Max .xlsx"
df = pd.read_excel(file_path, usecols=[0, 1, 2])

# Asegurarse de que 'Time' es un tipo de tiempo
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time

# Agrupar y calcular el tiempo mínimo y máximo para cada grupo
grouped = df.groupby(['Date', 'Emp ID']).agg(Min_Time=('Time', 'min'), Max_Time=('Time', 'max')).reset_index()

# Expandir los tiempos mínimo y máximo en filas separadas
min_times = grouped[['Date', 'Emp ID', 'Min_Time']].rename(columns={'Min_Time': 'Time'})
max_times = grouped[['Date', 'Emp ID', 'Max_Time']].rename(columns={'Max_Time': 'Time'})

expanded_df = pd.concat([min_times, max_times]).sort_values(by=['Date', 'Emp ID', 'Time'])

# Si es necesario resetear el índice
expanded_df.reset_index(drop=True, inplace=True)

print(expanded_df)
