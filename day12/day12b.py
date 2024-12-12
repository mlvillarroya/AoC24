
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
        region.sort()
        solution += region_area(region) * region_perimeter(region, content)
    print(solution)


    pass
def region_perimeter(region, entire_map):
    perimeter = 0
    perimeter_array = []
    for coordinate in region:
        row, column = coordinate
        if row==0:
            perimeter_array.append(("up",(0,column)))
        else:
            if entire_map[row-1][column]!=entire_map[row][column]:
                perimeter_array.append(("up", (row, column)))
        if row==len(entire_map)-1:
            perimeter_array.append(("down",(len(entire_map)-1,column)))
        else:
            if entire_map[row+1][column]!=entire_map[row][column]:
                perimeter_array.append(("down", (row, column)))
        if column==0:
            perimeter_array.append(("left",(row,0)))
        else:
            if entire_map[row][column-1]!=entire_map[row][column]:
                perimeter_array.append(("left", (row, column)))
        if column==len(entire_map[0])-1:
            perimeter_array.append(("right",(row,len(entire_map[0])-1)))
        else:
            if entire_map[row][column+1]!=entire_map[row][column]:
                perimeter_array.append(("right", (row, column)))
    directions = ["up", "down", "left", "right"]
    for direction in directions:
        same_direction_members = [member[1] for member in perimeter_array if member[0]==direction]
        if direction == "up" or direction == "down":
            same_direction_members.sort(key=lambda x: x[0])
        else:
            same_direction_members.sort(key=lambda x: x[1])
        while len(same_direction_members)>0:
            i = 0
            members_to_delete = [same_direction_members[0]]
            if direction == "up" or direction == "down":
                while i<len(same_direction_members)-1 and same_direction_members[i+1][0] == same_direction_members[i][0] and same_direction_members[i+1][1] == same_direction_members[i][1]+1:
                    members_to_delete.append(same_direction_members[i+1])
                    i+=1
            else:
                while i<len(same_direction_members)-1 and same_direction_members[i+1][1] == same_direction_members[i][1] and same_direction_members[i+1][0] == same_direction_members[i][0]+1:
                    members_to_delete.append(same_direction_members[i+1])
                    i+=1
            for member in members_to_delete:
                same_direction_members.remove(member)
            perimeter += 1
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