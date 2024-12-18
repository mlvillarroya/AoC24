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

    final_matrix = []
    for robot in data:
        final_matrix.append(move_robot(robot))
    how_many_robots = {0:0, 1:0, 2:0, 3:0, 4:0}
    for robot in final_matrix:
        how_many_robots[which_quadrant(robot[0], robot[1])]+=1
    print(how_many_robots[1]*how_many_robots[2]*how_many_robots[3]*how_many_robots[4])


def move_robot(robot_data):
    x, y, vx, vy = robot_data
    return (x + (TIMES*vx)%MATRIX_WIDTH)%MATRIX_WIDTH, (y + (TIMES*vy)%MATRIX_HEIGHT)%MATRIX_HEIGHT

def which_quadrant(x,y):
    mid_x = int(MATRIX_WIDTH/2)
    mid_y = int(MATRIX_HEIGHT/2)
    if (x<mid_x and y<mid_y):
        return 1
    elif (x>mid_x and y<mid_y):
        return 2
    elif (x<mid_x and y>mid_y):
        return 3
    elif (x>mid_x and y>mid_y):
        return 4
    else:
        return 0

if __name__ == "__main__":
    main()