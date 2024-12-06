class Navigator:
    def __init__(self, position):
        self.position = position
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

    def is_obstacle(self, position):
        return position in self.obstacles

def main():
    # Lee el contenido del archivo
    with open('data.txt', 'r') as archivo:
        content = archivo.read().split()
    my_map = My_map(content)
    navigator = Navigator(my_map.navigator_start_point)
    # convert content from a string array to an array of char arrays
    different_positions = 0
    visited_positions = set()
    while (0 <= navigator.position[0] < my_map.limit_row-1) and (0 <= navigator.position[1] < my_map.limit_columns - 1):
        new_pos = navigator.calculate_next_position()
        if new_pos in my_map.obstacles:
            navigator.turn()
        else:
            navigator.move(new_pos)
            if new_pos not in visited_positions:
                visited_positions.add(new_pos)
                different_positions += 1
    print(different_positions)

if __name__ == "__main__":
    main()