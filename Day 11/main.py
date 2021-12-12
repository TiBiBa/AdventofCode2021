
class Octopus:

    def __init__(self, energy):
        self.flashed = False
        self.energy = int(energy)

    def increase_energy(self):
        self.energy += 1

    def get_energy(self):
        return self.energy

    def get_flash(self):
        return self.flashed

    def flash(self):
        self.flashed = True

    def reset(self):
        self.flashed = False
        self.energy = 0


def get_neighbours(y, x):
    neighbours = []
    if x > 0:
        neighbours.append((y, x-1))
        if y > 0:
            neighbours.append((y-1, x-1))
    if x < 9:
        neighbours.append((y, x+1))
        if y > 0:
            neighbours.append((y-1, x+1))
    if y > 0:
        neighbours.append((y-1, x))
    if y < 9:
        neighbours.append((y+1, x))
        if x > 0:
            neighbours.append((y+1, x-1))
        if x < 9:
            neighbours.append((y+1, x+1))
    return neighbours


def step1():
    file = open("input.txt", "r")

    grid = []
    octopuses = file.read().splitlines()
    for y in range(0, len(octopuses)):
        row = []
        for x in range(0, len(octopuses[y])):
            octopus = Octopus(octopuses[y][x])
            row.append(octopus)
        grid.append(row)

    flashes = 0
    for _ in range(100):
        unflashed = True
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                grid[y][x].increase_energy()
        while unflashed:
            unflashed = False
            for y in range(0, len(grid)):
                for x in range(0, len(grid[y])):
                    if grid[y][x].get_energy() > 9 and not grid[y][x].get_flash():
                        unflashed = True
                        grid[y][x].flash()
                        flashes += 1
                        for neighbour in get_neighbours(y, x):
                            grid[neighbour[0]][neighbour[1]].increase_energy()
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x].get_flash():
                    grid[y][x].reset()
    print(flashes)

def step2():
    file = open("input.txt", "r")

    grid = []
    octopuses = file.read().splitlines()
    for y in range(0, len(octopuses)):
        row = []
        for x in range(0, len(octopuses[y])):
            octopus = Octopus(octopuses[y][x])
            row.append(octopus)
        grid.append(row)

    all_zero = False
    steps = 0
    while not all_zero:
        steps += 1
        unflashed = True
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                grid[y][x].increase_energy()
        while unflashed:
            unflashed = False
            for y in range(0, len(grid)):
                for x in range(0, len(grid[y])):
                    if grid[y][x].get_energy() > 9 and not grid[y][x].get_flash():
                        unflashed = True
                        grid[y][x].flash()
                        for neighbour in get_neighbours(y, x):
                            grid[neighbour[0]][neighbour[1]].increase_energy()
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x].get_flash():
                    grid[y][x].reset()

        all_zero = True
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x].get_energy() > 0:
                    all_zero = False
    print(steps)

step2()