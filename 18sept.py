import numpy as np
import matplotlib.pyplot as plt

# Arreglo de distribución normal con media 5 y desviación estandar 2 N(5,2)

arreglo = np.random.normal(size=1000000)*2 + 5

# tmb puedes usar un for para cambiar cada valor
# for i in arreglo: i*sigma+mu
plt.hist(arreglo, bins=100)
plt.show()
