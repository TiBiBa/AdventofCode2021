
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
        self.energy = 0


def get_neighbours(y, x):
    pass

def step(grid, flashes):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x].get_energy() > 9 and not grid[y][x].get_flash():
                grid[y][x].flash()
                for neighbours in get_neighbours(y, x):
                    flashes += step(grid, flashes+1)
            else:
                return flashes

    return grid, flashes

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
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                grid[y][x].increase_energy()
        grid, flashes = step(grid, flashes)

step1()