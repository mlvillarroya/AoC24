
def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read().split()
    numbers = [[int(i) for i in row] for row in [list(row) for row in content]]
    result = 0
    for i in range(len(numbers)):
        for j in range(len(numbers[0])):
            if numbers[i][j] == 0:
                result += how_many_paths(i, j, numbers)
                pass
    print(result)

def reach_nine(previous_number, current_row, current_column, entire_map):
    if current_row < 0 or current_row >= len(entire_map) or current_column < 0 or current_column >= len(entire_map[0]):
        return []
    if not entire_map[current_row][current_column] == previous_number + 1:
        return []
    if entire_map[current_row][current_column] == 9:
        return [(current_row, current_column)]
    else:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        result = []
        for direction in directions:
            new_row = current_row + direction[0]
            new_column = current_column + direction[1]
            result.extend(reach_nine(entire_map[current_row][current_column], new_row, new_column, entire_map))
        return result

def how_many_paths(current_row, current_column, entire_map):
    return len(reach_nine(-1, current_row, current_column, entire_map))

if __name__ == "__main__":
    main()