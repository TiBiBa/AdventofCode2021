file = open("input.txt", "r")
numbers = file.read().splitlines()
numbers = [int(i) for i in numbers]

for i in range(0, len(numbers)):
    for j in range(i, len(numbers)):
        for k in range(j, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i] * numbers[j] * numbers[k])