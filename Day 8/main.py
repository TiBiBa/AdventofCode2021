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
    for i in range(0, 10):
        decoder[i] = ""
    return decoder

def step2():
    file = open("input.txt", "r")
    puzzles = file.read().splitlines()

    counter = 0
    puzzle_count = 0
    for puzzle in puzzles:
        numbers = get_empty_decoder()

        puzzle_input = puzzle.split("|")[0].split()
        puzzle_input = [''.join(sorted(x)) for x in puzzle_input]

        puzzle_output = puzzle.split("|")[1].split()
        puzzle_output = [''.join(sorted(x)) for x in puzzle_output]

        letters = "abcdefg"

        #Get the numbers we know for sure
        for number in puzzle_input:
            if len(number) == 2:
                numbers[1] = number
            elif len(number) == 3:
                numbers[7] = number
            elif len(number) == 4:
                numbers[4] = number
            elif len(number) == 7:
                numbers[8] = number

        #Find the 6 by looking if a len(6) has a bit that the 7 does NOT have
        for number in puzzle_input:
            if len(number) == 6:
                for char in numbers[7]:
                    if char not in number:
                        numbers[6] = number

        #Find the 2, 3 and 5 (They are all 5 char long)
        for number in puzzle_input:
            if len(number) == 5:
                temp = numbers[6]
                for char in number:
                    temp = temp.replace(char, "")
                if len(temp) == 1:
                    numbers[5] = number
                elif len(temp) == 2:
                    for sub_char in temp:
                        if sub_char in numbers[1]:
                            numbers[2] = number
                    if (numbers[2] != number):
                        numbers[3] = number

        #Find the 0 and 9
        for number in puzzle_input:
            if len(number) == 6:
                temp = number
                for char in numbers[4]:
                    temp = temp.replace(char, "")
                if len(temp) == 2:
                    numbers[9] = number
                elif (numbers[6] != number):
                    numbers[0] = number

        number_string = ""
        for decoded_number in puzzle_output:
            for key, char_string in numbers.items():
                if decoded_number == char_string:
                    number_string += str(key)

        counter += int(number_string)
    print(counter)

step2()