import numpy as np

# Lee el contenido del archivo
with open('data.txt', 'r') as archivo:
    contenido = archivo.read().split("\n")
    matriz = [[int(num) for num in fila.split()] for fila in contenido if fila]

# Convierte la lista en un array NumPy
matriz_np = np.array(matriz)

# Trasponer la matriz
matriz_transpuesta = matriz_np.T

row1 = np.sort(matriz_transpuesta[0])
row2 = np.sort(matriz_transpuesta[1])
suma=0
for i in range(len(row1)):
    suma += abs(row1[i]-row2[i])

print(suma)