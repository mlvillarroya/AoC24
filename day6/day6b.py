class Navigator:
    def __init__(self, initial_position):
        self.initial_position = initial_position
        self.position = initial_position
        self.round = 0

    def calculate_next_position(self):
        if self.round == 0: return self.position[0] - 1, self.position[1]  #UP
        elif self.round == 1: return self.position[0], self.position[1] + 1  #RIGHT
        elif self.round == 2: return self.position[0] + 1, self.position[1]  #DOWN
        elif self.round == 3: return self.position[0], self.position[1] - 1  #LEFT

    def move(self, position):
        self.position = position

    def turn(self):
        self.round = (self.round+1)%4

    def restart_navigator(self):
        self.position = self.initial_position
        self.round = 0


class My_map:
    def __init__(self, content):
        self.obstacles = set()
        self.content = content
        self.limit_row = len(content[0])
        self.limit_columns = len(content)
        for i in range(len(content)):
            for j in range(len(content[i])):
                if content[i][j] == '#':
                    self.add_obstacle((i, j))
                elif content[i][j] == '^':
                    self.navigator_start_point = (i, j)

    def add_obstacle(self, obstacle):
        self.obstacles.add(obstacle)

    def remove_obstacle(self, obstacle):
        self.obstacles.remove(obstacle)

    def is_obstacle(self, position):
        return position in self.obstacles

def walk_trough_map_loop(navigator, my_map):
    visited_positions = set()
    while (0 <= navigator.position[0] < my_map.limit_row-1) and (0 <= navigator.position[1] < my_map.limit_columns - 1):
        new_pos = navigator.calculate_next_position()
        if new_pos in my_map.obstacles:
            navigator.turn()
        else:
            navigator.move(new_pos)
            if (navigator.round,new_pos) in visited_positions: return True
            visited_positions.add((navigator.round, new_pos))
    return False

def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read().split()
    my_map = My_map(content)
    navigator = Navigator(my_map.navigator_start_point)

    different_positions = 0
    for i in range(my_map.limit_row):
        for j in range(my_map.limit_columns):
            if not my_map.is_obstacle((i,j)):
                my_map.add_obstacle((i,j))
                if walk_trough_map_loop(navigator, my_map):
                    different_positions += 1
                my_map.remove_obstacle((i,j))
                navigator.restart_navigator()

    print(different_positions)


if __name__ == "__main__":
    main()