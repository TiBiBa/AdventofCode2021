import numpy as np


def initialize_grid():
    file = open("input.txt", "r")
    file_data = file.read().splitlines()

    dot_locations = []
    fold_instructions = []
    instructions = False

    for line in file_data:
        if len(line.strip()) > 0 and not instructions:
            dot_locations.append(line)
        elif instructions:
            fold_instructions.append(line)
        else:
            instructions = True

    coordinates = []
    max_x = 0
    max_y = 0

    for location in dot_locations:
        location = location.split(",")
        if len(location) == 2:
            if int(location[0]) > max_x:
                max_x = int(location[0])
            if int(location[1]) > max_y:
                max_y = int(location[1])
            coordinates.append([int(location[0]), int(location[1])])
    grid = np.zeros((max_x+1, max_y+1))
    for coordinate in coordinates:
        grid[coordinate[0]][coordinate[1]] = 1
    return grid, fold_instructions


def fold(grid, axis, instruction):
    grid = grid.copy()
    if axis == "x":
        part1 = grid[:instruction, :]
        part2 = np.flipud(grid[instruction+1:, :])

    else:
        part1 = grid[:, :instruction]
        part2 = np.fliplr(grid[:, instruction+1:])

    grid = np.add(part1, part2)
    grid[grid > 1] = 1
    return grid


def step1():
    grid, fold_instructions = initialize_grid()

    axis = fold_instructions[0].split(" ")[2].split("=")[0]
    instruction = int(fold_instructions[0].split(" ")[2].split("=")[1])
    grid = fold(grid, axis, instruction)
    print(np.count_nonzero(grid))


def step2():
    grid, fold_instructions = initialize_grid()

    for fold_instruction in fold_instructions:
        axis = fold_instruction.split(" ")[2].split("=")[0]
        instruction = int(fold_instruction.split(" ")[2].split("=")[1])
        grid = fold(grid, axis, instruction)

    grid[grid == 0] = 'nan'
    np.set_printoptions(nanstr=".")
    print(grid)


step2()