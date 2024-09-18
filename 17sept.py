import numpy as np
arr_2d = np.zeros((5,10))

for i,fila in enumerate(arr_2d):
    for j,columna in enumerate(fila):
        arr_2d[i][j] = len(fila) * i + j

# determine dimension y forma
print(f'dimension = {arr_2d.ndim} y forma = .shape')

print(':\n', arr_2d.T)

arr_2d[:, 4] = 999
print(arr_2d)

arr_2d[2:4, :] = -5
print(arr_2d)

# yay





