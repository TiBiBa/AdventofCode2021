file = open("input.txt", "r")
actions = file.readlines()

#step 1
horizontal = 0
depth = 0
for action in actions:
    direction = action.split()[0]
    amount = int(action.split()[1])
    if direction == 'forward':
        horizontal += amount
    elif direction == 'down':
        depth += amount
    elif direction == 'up':
        depth -= amount
print(horizontal * depth)

print("****************************************")

#step 2
horizontal = 0
depth = 0
aim = 0
for action in actions:
    direction = action.split()[0]
    amount = int(action.split()[1])
    if direction == 'forward':
        horizontal += amount
        depth += (aim * amount)
    elif direction == 'down':
        aim += amount
    elif direction == 'up':
        aim -= amount
print(horizontal * depth)

