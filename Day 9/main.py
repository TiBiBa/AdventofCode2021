class Valve:

    up = 999
    right = 999
    down = 999
    left = 999

    def __init__(self, height):
        self.height = int(height)
        self.visited = False

    def set_up_neighbour(self, up):
        self.up = int(up)

    def set_right_neighbour(self, right):
        self.right = int(right)

    def set_down_neighbour(self, down):
        self.down = int(down)

    def set_left_neighbour(self, left):
        self.left = int(left)

    def set_visited(self):
        self.visited = True

    def get_visited(self):
        return self.visited

    def get_neighbours(self):
        return self.up, self.right, self.down, self.left

    def get_height(self):
        return self.height

    def is_lowest_point(self):
        if self.height < min([self.up, self.right, self.down, self.left]):
            return True

    def get_risk_level(self):
        return self.height + 1


def createValves():
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
    return valves2dArray


def step1():
    valves2dArray = createValves()

    risk_counter = 0
    for y in range(0, len(valves2dArray)):
        for x in range(0, len(valves2dArray[y])):
             if valves2dArray[y][x].is_lowest_point():
                 risk_counter += valves2dArray[y][x].get_risk_level()
    print(risk_counter)


def walk(valves, current_y, current_x, direction, current_size):
    if direction == 'up':
        if current_y > 0 and valves[current_y-1][current_x].get_height() < 9 and not valves[current_y-1][current_x].get_visited():
            valves[current_y - 1][current_x].set_visited()
            return walk(valves, (current_y-1), current_x, None, (current_size+1))
        else:
            return current_size
    elif direction == 'right':
        if current_x < (len(valves[current_y])-1) and valves[current_y][current_x+1].get_height() < 9 and not valves[current_y][current_x+1].get_visited():
            valves[current_y][current_x + 1].set_visited()
            return walk(valves, current_y, (current_x+1), None, (current_size+1))
        else:
            return current_size
    elif direction == 'left':
        if current_x > 0 and valves[current_y][current_x-1].get_height() < 9 and not valves[current_y][current_x-1].get_visited():
            valves[current_y][current_x - 1].set_visited()
            return walk(valves, current_y, (current_x-1), None, (current_size+1))
        else:
            return current_size
    elif direction == 'down':
        if current_y < (len(valves) - 1) and valves[current_y+1][current_x].get_height() < 9 and not valves[current_y+1][current_x].get_visited():
            valves[current_y+1][current_x].set_visited()
            return walk(valves, (current_y+1), current_x, None, (current_size + 1))
        else:
            return current_size
    else:
        for direction in ['up', 'right', 'down', 'left']:
            current_size = walk(valves, current_y, current_x, direction, current_size)

    return current_size

def step2():
    valves2dArray = createValves()
    bin_sizes = []

    for y in range(0, len(valves2dArray)):
        for x in range(0, len(valves2dArray[y])):
            bin_sizes.append(walk(valves2dArray, y, x, None, 0))
    bin_sizes.sort(reverse=True)
    biggest_bins = bin_sizes[:3]
    counter = 1
    for bin in biggest_bins:
        counter *= bin
    print(counter)

step2()