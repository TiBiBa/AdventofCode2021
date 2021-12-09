class Valve:

    up = 999
    right = 999
    down = 999
    left = 999

    def __init__(self, height):
        self.height = int(height)

    def set_up_neighbour(self, up):
        self.up = int(up)

    def set_right_neighbour(self, right):
        self.right = int(right)

    def set_down_neighbour(self, down):
        self.down = int(down)

    def set_left_neighbour(self, left):
        self.left = int(left)

    def get_neighbours(self):
        return self.up, self.right, self.down, self.left

    def get_height(self):
        return self.height

    def is_lowest_point(self):
        if self.height < min([self.up, self.right, self.down, self.left]):
            return True

    def get_risk_level(self):
        return self.height + 1

def step1():
    file = open("input.txt", "r")
    temp = file.read().splitlines()
    heights = []
    for height in temp:
        heights.append(list(height))

    valves2dArray = []

    for y in range(0, len(heights)):
        valveRow = []
        for x in range(0, len(heights[y])):
            valve = Valve(heights[y][x])
            if x > 0:
                valve.set_left_neighbour(heights[y][x-1])
            if x < (len(heights[y])-1):
                valve.set_right_neighbour(heights[y][x+1])
            if y > 0:
                valve.set_up_neighbour(heights[y-1][x])
            if y < (len(heights) - 1):
                valve.set_down_neighbour(heights[y+1][x])
            valveRow.append(valve)
        valves2dArray.append(valveRow)

    risk_counter = 0
    for y in range(0, len(valves2dArray)):
        for x in range(0, len(valves2dArray[y])):
             if valves2dArray[y][x].is_lowest_point():
                 risk_counter += valves2dArray[y][x].get_risk_level()
    print(risk_counter)


def walk(heights, current_y, current_x, basin_size):
    for direction in ['up', 'right', 'down', 'left']:
        basin_size += walkDirection(heights, current_y, current_x, direction, basin_size)
    return basin_size


def walkDirection(heights, current_y, current_x, direction, basin_size):
    if direction == 'left' and current_x > 0 and heights[current_y][current_x-1] < 9:
        return walk(heights, current_y, current_x-1, basin_size+1)
    elif direction == 'up' and current_y > 0 and heights[current_y-1][current_x] < 9:
        return walk(heights, current_y+1, current_x, basin_size+1)

    else:
        return basin_size

def step2():
    file = open("input.txt", "r")
    temp = file.read().splitlines()
    heights = []
    for height in temp:
        heights.append(list(height))

    for y in range(0, len(heights)):
        for x in range(0, len(heights[y])):
            if heights[y][x] < 9:
                print(walk(heights, y, x, 0))