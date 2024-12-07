from itertools import product

def operate(a, b, op):
    if op == '+':
        return a+b
    elif op == '*':
        return a*b
    else:
        raise ValueError("Operador no valido")

def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read().split('\n')
    content = [row.split() for row in content]
    total_result = 0
    for row in content:
        result_to_check = int(row[0][:-1])
        numbers_to_check = [int(number) for number in row[1:]]
        for op_possibility in product("+*", repeat=len(numbers_to_check)-1):
            result = numbers_to_check[0]
            match = False
            for i in range(len(op_possibility)):
                result = operate(result, numbers_to_check[i+1], op_possibility[i])
            if result == result_to_check:
                match = True
            if match:
                total_result += result_to_check
                break

    print(total_result)

if __name__ == "__main__":
    main()