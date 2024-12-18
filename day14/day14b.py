import re
MATRIX_WIDTH = 101
MATRIX_HEIGHT = 103
TIMES = 100

def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        full_content = archivo.read()
    pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    data = [[int(x) for x in row] for row in re.findall(pattern, full_content)]
    create_file("test.txt")
    for times in range(1, 7000):
        final_matrix = []
        for robot in data:
            final_matrix.append(move_robot(robot, times))
        if look_for_pattern(final_matrix, 10):
            print(f"Time: {times}")
            print_matrix(final_matrix)
            break
    print("Done")



def move_robot(robot_data, times):
    x, y, vx, vy = robot_data
    return (x + (times*vx)%MATRIX_WIDTH)%MATRIX_WIDTH, (y + (times*vy)%MATRIX_HEIGHT)%MATRIX_HEIGHT

def look_for_pattern(matrix, how_many_checks):
    for row in range(MATRIX_HEIGHT):
        checks_in_a_row = 0
        for col in range(MATRIX_WIDTH):
            if (col, row) in matrix:
                checks_in_a_row += 1
                if checks_in_a_row >= how_many_checks:
                    return True
            else:
                checks_in_a_row = 0

    return False

def print_matrix(matrix):
    for row in range(MATRIX_HEIGHT):
        for col in range(MATRIX_WIDTH):
            if (col, row) in matrix:
                print("#", end="")
            else:
                print(".", end="")
        print()

def print_matrix_in_file(number, matrix, filename):
    with open(filename, 'a') as archivo:
        archivo.write(f"Time: {number}\n")
        for row in range(MATRIX_HEIGHT):
            for col in range(MATRIX_WIDTH):
                if (col, row) in matrix:
                    archivo.write("#")
                else:
                    archivo.write(".")
            archivo.write("\n")
        archivo.write("\n")

def create_file(filename):
    with open(filename, 'w') as archivo:
        archivo.write("")

if __name__ == "__main__":
    main()