# create a enum for up, down, left, right
import enum

class Direction(enum.Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        map, instructions = archivo.read().split("\n\n")
    map = [list(line) for line in map.split("\n")]
    instructions = ("").join(instructions.split("\n"))
    robot_position = find_robot(map)
    for instruction in instructions:
        direction = read_direction(instruction)
        map, robot_position = move_robot(map, robot_position, direction)
    sum = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'O':
                sum += 100*i + j
    print(sum)


def find_robot(matrix):
    column = 0
    for row in range(len(matrix)):
        if '@' in matrix[row]:
            column = matrix[row].index('@')
            return row, column
    return -1, -1


def move_robot(matrix, robot_position, direction: Direction):
    row, col = robot_position
    next_col, next_row = go_forward_with_direction(col, direction, row)

    # Check for walls
    if matrix[next_row][next_col] == '#':
        return matrix, (row, col)

    # If the next cell is empty, move the robot
    if matrix[next_row][next_col] == '.':
        matrix[next_row][next_col] = '@'
        matrix[row][col] = '.'
        return matrix, (next_row, next_col)

    # If the next cell has a package, attempt to push it
    if matrix[next_row][next_col] == 'O':
        while matrix[next_row][next_col] == 'O':
            next_col, next_row = go_forward_with_direction(next_col, direction, next_row)
        if matrix[next_row][next_col] == '#':
            return matrix, (row, col)
        else:
            while next_col != col or next_row != row:
                prev_col, prev_row = go_backwards_with_direction(next_col, direction, next_row)
                matrix[next_row][next_col] = matrix[prev_row][prev_col]
                next_col, next_row = prev_col, prev_row
            matrix[row][col] = '.'
        next_col, next_row = go_forward_with_direction(next_col, direction, next_row)
        return matrix, (next_row, next_col)

def go_forward_with_direction(col, direction, row):
    if direction == Direction.UP:
        next_row = row - 1
        next_col = col
    elif direction == Direction.DOWN:
        next_row = row + 1
        next_col = col
    elif direction == Direction.LEFT:
        next_row = row
        next_col = col - 1
    elif direction == Direction.RIGHT:
        next_row = row
        next_col = col + 1
    else:
        raise ValueError("Invalid direction")
    return next_col, next_row

def go_backwards_with_direction(col, direction, row):
    if direction == Direction.UP:
        next_row = row + 1
        next_col = col
    elif direction == Direction.DOWN:
        next_row = row - 1
        next_col = col
    elif direction == Direction.LEFT:
        next_row = row
        next_col = col + 1
    elif direction == Direction.RIGHT:
        next_row = row
        next_col = col - 1
    else:
        raise ValueError("Invalid direction")
    return next_col, next_row

def read_direction(instruction) -> Direction:
    if instruction == '^':
        return Direction.UP
    elif instruction == 'v':
        return Direction.DOWN
    elif instruction == '<':
        return Direction.LEFT
    elif instruction == '>':
        return Direction.RIGHT
    else:
        raise ValueError(f"{instruction} is an Invalid instruction")

if __name__ == "__main__":
    main()