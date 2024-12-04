MISTERY_WORD = "MAS"
CENTER_WORD = "A"

def found_mistery_cross(coord_x, coord_y, letter_matrix):
    if letter_matrix[coord_x][coord_y] != CENTER_WORD:
        return False
    if coord_x == 0 or coord_x == len(letter_matrix) - 1 or coord_y == 0 or coord_y == len(letter_matrix[0]) - 1:
        return False
    if sorted(letter_matrix[coord_x - 1][coord_y - 1] + letter_matrix[coord_x][coord_y] + letter_matrix[coord_x + 1][coord_y + 1]) != sorted(MISTERY_WORD):
        return False
    if sorted(letter_matrix[coord_x - 1][coord_y + 1] + letter_matrix[coord_x][coord_y] + letter_matrix[coord_x + 1][coord_y - 1]) != sorted(MISTERY_WORD):
        return False
    return True

def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read().split()
    result = 0
    for i in range(len(content)):
        for j in range(len(content[i])):
            result += found_mistery_cross(i, j, content)
    print(result)

if __name__ == "__main__":
    main()