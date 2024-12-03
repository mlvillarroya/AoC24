import re


def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read()
    patron = re.compile(r"mul\((\d+)\,(\d+)\)")
    elements = [[int(x), int(y)] for x, y in patron.findall(content)]
    result = 0
    for element in elements:
        result += element[0] * element[1]
    print(result)


if __name__ == "__main__":
    main()