# Lee el contenido del archivo
with open('data.txt', 'r') as archivo:
    contenido = [list(map(int, fila.split())) for fila in archivo if fila.strip()]

# Separar las listas en dos listas individuales
left_list, right_list = zip(*contenido)

# Ordenar ambas listas
left_list_sorted = sorted(left_list)
right_list_sorted = sorted(right_list)

# Calcular la suma de las diferencias absolutas
suma = sum(abs(l - r) for l, r in zip(left_list_sorted, right_list_sorted))

print(suma)
