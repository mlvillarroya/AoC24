import numpy as np
import re

def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        full_content = archivo.read()
    situations = read_content(full_content)
    solutions = []
    for situation in situations:
        a, b = solve_equation(situation)
        if (a%1 < 0.001 or a%1>0.999) and (b%1 < 0.001 or b%1 > 0.999) :
            solutions.append((int(round(a)), int(round(b))))
    result = 0
    for solution in solutions:
        result += 3*solution[0] + solution[1]
    print(result)

def solve_equation(situation):
    a = np.array([[situation[0], situation[2]], [situation[1], situation[3]]])
    b = np.array([situation[4]+10000000000000, situation[5]+10000000000000])
    x = np.linalg.solve(a, b)
    a, b = x
    return a, b

def read_content(full_content):
    regex = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    pattern = re.compile(regex)
    situations = pattern.findall(full_content)
    situations = [(int(a), int(b), int(c), int(d), int(e), int(f)) for a, b, c, d, e, f in situations]
    return situations

if __name__ == "__main__":
    main()