import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1. Genera un arreglo 1D, llamado freq, de 4 elementos de números aleatorios enteros en el intervalo [1, 8]

freq = np.random.randint(1,8, size = 4)
print(freq)

# Ejercicio 2. Genera un arreglo 1D, llamado amplitud, de 4 elementos de números aleatorios con distribución uniforme
# en el intervalo [3, 6]

amplitud = np.random.uniform(3,6,size=4)
print(amplitud)

# Ejercicio 3. Use el metodo arange para generar un arreglo, llamado t, de 2000 números en el intervalo [0, 1]

t = np.arange(0,1,1/2000)
print(t)

# Ejercicio 4. Genere 4 ondas sinusoidales con cada frecuencia y amplitud.
# Hint: recuerde que la ecuación de la onda sinusoidal es y(t) = A*sin(2*piB*t) donde A es la amplitud y B es la
# frecuencia. Para usar pi en numpy, use np.pi
# Sugerencia: para visualizar las ondas sinusoidales puede usar las líneas de código


onda = [A * np.sin(2 * np.pi * B * t) for A, B in zip(amplitud, freq)]

plt.figure(figsize=(10, 8))
for i, o in enumerate(onda):
    plt.plot(t, o, label=f'Onda {i+1}')
plt.show()

# Ejercicio 5. Cree un arreglo llamado x, que sea la suma de las 4 ondas sinusoidales

x = np.sum(onda, axis=0)
print(x)

# Numpy también permite aplicar operadores tales como la transormada de fourier a un arreglo de datos con
# el paquete np.fft, en particular la función np.fft.fft(x) aplica la transformada discreta de fourier al arreglo x

fft_x = np.fft.fft(x)

# Ejercicio 6. Cree un arreglo, llamado frequence, de los enteros en el intervalo [0, 1999]
frequence = np.arange(2000)
print(frequence)

# Ejercicio 7. Calcular el valor absoluto a todos los elementos del arreglo X
absx = np.abs(x)
print(absx)

# Ejercicio 8. De los primeros 10 elementos del arreglo del ejercicio anterior, determine los 4 elementos máximos y en
# qué índices se localizan

i_max = np.argsort(absx[:10])[-4:]
i_max = i_max[::-1]
print(i_max)
valores_max=absx[:10][i_max]
print(valores_max)
