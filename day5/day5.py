import re

def is_sorted(elements, order_array):
    for order_row in order_array:
        try:
            first_element_index = elements.index(order_row[0])
            if order_row[1] in elements[:first_element_index]:
                return False
        except:
            continue
    return True


def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read()
    part1, part2 = content.split('\n\n')
    part1 = [[int(x), int(y)] for x, y in [row.split('|') for row in part1.split('\n')]]
    part2 = [[int(x) for x in elements] for elements in [row.split(',') for row in part2.split('\n')]]

    result = 0
    for element in part2:
        if is_sorted(element,part1):
            result += element[len(element)//2]
    print(result)




if __name__ == "__main__":
    main()