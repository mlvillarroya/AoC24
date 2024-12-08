
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
                    antinodes = calculate_antinodes(symbols[j][1], symbol[1])
                    for antinode in antinodes:
                        if antinode_inside(antinode[0], antinode[1], content):
                            antinodes_set.add(antinode)
    print(len(antinodes_set))

def calculate_antinodes(coord1, coord2):
        row1, col1 = coord1
        row2, col2 = coord2
        dist = (row2-row1, col2-col1)
        return (row1-dist[0], col1-dist[1]), (row2+dist[0], col2+dist[1])

def antinode_inside(antinode_row, antinode_col, content):
    return antinode_row >= 0 and antinode_row < len(content) and antinode_col >= 0 and antinode_col < len(content[0])

if __name__ == "__main__":
    main()