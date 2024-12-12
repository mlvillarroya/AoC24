
def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content =  [list(row) for row in archivo.read().split()]
    content_visited = set()
    different_regions=[]
    for i in range(len(content)):
        for j in range(len(content[i])):
            if (i, j) not in content_visited:
                region = explore_zone(set(), i, j, content)
                different_regions.append(region)
                content_visited.update(region)
    solution = 0
    for region in different_regions:
        solution += region_area(region) * region_perimeter(region, content)
    print(solution)


    pass
def region_perimeter(region, entire_map):
    perimeter = 0
    for coordinate in region:
        row, column = coordinate
        if row==0: perimeter+=1
        else:
            if entire_map[row-1][column]!=entire_map[row][column]: perimeter+=1
        if row==len(entire_map)-1: perimeter+=1
        else:
            if entire_map[row+1][column]!=entire_map[row][column]: perimeter+=1
        if column==0: perimeter+=1
        else:
            if entire_map[row][column-1]!=entire_map[row][column]: perimeter+=1
        if column==len(entire_map[0])-1: perimeter+=1
        else:
            if entire_map[row][column+1]!=entire_map[row][column]: perimeter+=1
    return perimeter



def region_area(region):
    return len(region)

def explore_zone(visited_nodes, current_row, current_column, entire_map):
    sign = entire_map[current_row][current_column]
    visited_nodes.add((current_row, current_column))
    result = []

    if current_row > 0 and entire_map[current_row - 1][current_column] == sign and (current_row - 1, current_column) not in visited_nodes:
        result.extend(explore_zone(visited_nodes, current_row - 1, current_column, entire_map))
    if current_row < len(entire_map) - 1 and entire_map[current_row + 1][current_column] == sign and (current_row + 1, current_column) not in visited_nodes:
        result.extend(explore_zone(visited_nodes, current_row + 1, current_column, entire_map))
    if current_column > 0 and entire_map[current_row][current_column - 1] == sign and (current_row, current_column - 1) not in visited_nodes:
        result.extend(explore_zone(visited_nodes, current_row, current_column - 1, entire_map))
    if current_column < len(entire_map[0]) - 1 and entire_map[current_row][current_column + 1] == sign and (current_row, current_column + 1) not in visited_nodes:
        result.extend(explore_zone(visited_nodes, current_row, current_column + 1, entire_map))

    result.append((current_row, current_column))
    return result


if __name__ == "__main__":
    main()