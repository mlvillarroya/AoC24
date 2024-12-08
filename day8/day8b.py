
def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read().split('\n')

    symbols = []
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] != '.':
                symbols.append((content[i][j],(i,j)))

    antinodes_set = set()

    for i in range(len(symbols)):
        symbol = symbols[i]
        for j in range(len(symbols)):
            if i != j:
                if symbols[j][0] == symbol[0]:
                    antinodes = calculate_antinodes(symbols[j][1], symbol[1], content)
                    for antinode in antinodes:
                        antinodes_set.add(antinode)
    print(len(antinodes_set))

def calculate_antinodes(coord1, coord2, content):
        row1, col1 = coord1
        row2, col2 = coord2
        dist = (row2-row1, col2-col1)
        result = [coord1, coord2]
        i=0
        while True:
            i+=1
            new_antinode = (row2+i*dist[0], col2+i*dist[1])
            if antinode_inside(new_antinode[0], new_antinode[1], content):
                result.append(new_antinode)
            else:
                break
        i=0
        while True:
            i+=1
            new_antinode = (row1-i*dist[0], col1-i*dist[1])
            if antinode_inside(new_antinode[0], new_antinode[1], content):
                result.append(new_antinode)
            else:
                break
        return result

def antinode_inside(antinode_row, antinode_col, content):
    return antinode_row >= 0 and antinode_row < len(content) and antinode_col >= 0 and antinode_col < len(content[0])

if __name__ == "__main__":
    main()