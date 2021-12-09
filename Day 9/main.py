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
             print(valves2dArray[y][x].get_height())
             print(valves2dArray[y][x].get_neighbours())
             if valves2dArray[y][x].is_lowest_point():
                 risk_counter += valves2dArray[y][x].get_risk_level()
    print(risk_counter)

step1()