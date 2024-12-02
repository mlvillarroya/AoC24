import numpy as np

def row_is_safe(row):
    slope = 1 if row[0] < row[1] else -1
    for i in range(len(row)-1):
        difference = slope * (row[i+1]  - row[i])
        if difference < 1 or difference > 3: return False
    return True

def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read().split("\n")
        matrix = [[int(num) for num in row.split()] for row in content if row]
    result = 0
    for row in matrix:
        if row_is_safe(row):
            result += 1
    print(result)


if __name__ == "__main__":
    main()