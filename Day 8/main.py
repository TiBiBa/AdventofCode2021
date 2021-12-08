def step1():
    file = open("input.txt", "r")
    digits = file.read().splitlines()
    counter = 0
    for combi in digits:
        output = combi.split("|")[1]
        for number in output.split():
            if len(number) in [2, 3, 4, 7]:
                counter += 1
    print("Amount of either 1, 4, 7 or 8: " + str(counter))

def get_empty_decoder():
    decoder = {}
    for i in range(1, 8):
        decoder[i] = ""
    return decoder

def step2():
    file = open("input.txt", "r")
    puzzles = file.read().splitlines()
    for puzzle in puzzles:
        decoder = get_empty_decoder()
        numbers = get_empty_decoder()

        puzzle_input = puzzle.split("|")[0].split()
        puzzle_input = [''.join(sorted(x)) for x in puzzle_input]

        puzzle_output = puzzle.split("|")[1].split()
        puzzle_output = [''.join(sorted(x)) for x in puzzle_output]

        for number in puzzle_input:
            if len(number) == 2:
                numbers[1] = number
            elif len(number) == 3:
                numbers[7] = number
            elif len(number) == 4:
                numbers[4] = number
            elif len(number) == 7:
                numbers[8] = number
        decoder[1] = numbers[7]
        for char in numbers[1]:
            if char in decoder[1]:
                decoder[1] = decoder[1].replace(char, '')
        print(decoder)

step2()