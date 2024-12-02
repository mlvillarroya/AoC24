from array import array

import numpy as np

def count_number(number, test_array):
    count = 0
    for i in test_array:
        if i == number:
            count += 1
    return count

# Lee el contenido del archivo
with open('data.txt', 'r') as archivo:
    contenido = archivo.read().split("\n")
    matriz = [[int(num) for num in fila.split()] for fila in contenido if fila]

# Convierte la lista en un array NumPy
matriz_np = np.array(matriz).T
sum = 0
for number in matriz_np[0]:
    sum+=number * count_number(number, matriz_np[1])

print(sum)

