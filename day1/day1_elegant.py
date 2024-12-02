import numpy as np

# Lee el contenido del archivo y convierte en un array NumPy
matriz_np = np.loadtxt('data.txt', dtype=int)

# Trasponer y ordenar las filas
matriz_transpuesta = np.sort(matriz_np.T)

# Calcular la suma de las diferencias absolutas
suma = np.sum(np.abs(matriz_transpuesta[0] - matriz_transpuesta[1]))

print(suma)
