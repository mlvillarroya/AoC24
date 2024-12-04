import re

MISTERY_WORD = "XMAS"

def found_mistery_word(letter_array, x_coord, y_coord, direction_x, direction_y):
    for i in range(len(MISTERY_WORD)):
        if x_coord < 0 or x_coord >= len(letter_array[0]) or y_coord < 0 or y_coord >= len(letter_array):
            return False
        if letter_array[y_coord][x_coord] != MISTERY_WORD[i]:
            return False
        x_coord += direction_x
        y_coord += direction_y
    return True


def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read().split()
    result = 0
    for i in range(len(content)):
        for j in range(len(content[i])):
            result += found_mistery_word(content, j, i, 1, 0) + \
                        found_mistery_word(content, j, i, 0, 1) + \
                        found_mistery_word(content, j, i, 1, 1) + \
                        found_mistery_word(content, j, i, -1, 1) + \
                        found_mistery_word(content, j, i, 1, -1) + \
                        found_mistery_word(content, j, i, -1, -1) + \
                        found_mistery_word(content, j, i, 0, -1) + \
                        found_mistery_word(content, j, i, -1, 0)
    print(result)





if __name__ == "__main__":
    main()