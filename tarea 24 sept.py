import pandas as pd

# Ejercicio 1. Mediante teclado especificar los siguiente:

# - Numero de columnas que tendrá el dataframe
num_columns = int(input("¿Cuántas columnas tendrá el DataFrame? "))

# - Una vez que se especifique, preguntar por los datos que tendra esa Serie
data = []
for i in range(num_columns):
    column_data = input(f"Introduce los datos para la columna {i+1} (separados por comas): ").split(',')
    data.append(column_data)

# - Preguntar por los nombres de las columnas que tendrá el dataframe
column_names = input("Introduce los nombres de las columnas separados por comas: ").split(',')

# - Preguntar por los nombres de las filas que tendrá el dataframe
row_names = input("Introduce los nombres de las filas separados por comas: ").split(',')

# - Una vez introducidos los datos, crear el dataframe que contenga esa información

df = pd.DataFrame(data).T
df.columns = column_names
df.index = row_names

# - Mostrar el dataframe

print(df)