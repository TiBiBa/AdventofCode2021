file = open("input.txt", "r")
passwords = file.read().splitlines()

valid = 0

for password in passwords:
    bounds = password.split(" ")
    lower_bound = int(bounds[0].split("-")[0])
    upper_bound = int(bounds[0].split("-")[1])
    char = bounds[1][:-1]
    pwd = bounds[2]
    if (pwd[lower_bound-1] == char and pwd[upper_bound-1] != char) or (pwd[lower_bound-1] != char and pwd[upper_bound-1] == char):
        valid += 1
print(valid)