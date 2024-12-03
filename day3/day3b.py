import re


def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read()
    patron = re.compile(r"mul\((\d+),(\d+)+\)|(do)\(\)|(don)\'t\(\)")
    elements = patron.findall(content)

    activated = True
    result = 0
    for element in elements:
        if activated and element[0] != '' and element[1] != '':
            result += int(element[0]) * int(element[1])
        elif not activated and element[2] != '':
            activated = True
        elif activated and element[3] != '':
            activated = False

    print(result)


if __name__ == "__main__":
    main()