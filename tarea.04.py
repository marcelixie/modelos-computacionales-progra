# Ejercicio 1

calif_1 = 10
calif_2 = 7
calif_3 = 4

# La primera nota vale un 15% del total. La segunda nota vale un 35% del total. La tercera nota vale un 50% del total
total = (0.15*calif_1) + (0.35*calif_2) + (0.50*calif_3)
print("La calificación final es:", total)

# Ejercicio 2
# La siguiente matriz debe cumplir que el 4to valor de cada fila debe ser igual a la suma de los primeros 3 valores. Crea un código para hacer las correcciones necesarias
matriz = [ [1, 1, 1, 3],
           [2, 2, 2, 7],
           [3, 3, 3, 9],
           [4, 4, 4, 13] ]

for fila in matriz:
    suma = sum(fila[:3])
    fila[3] = suma

print(matriz)


