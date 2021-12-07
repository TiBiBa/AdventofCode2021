from collections import Counter

def step1():
  file = open("input.txt", "r")
  lanternfishes = file.readline().split(",")
  lanternfishes = [int(i) for i in lanternfishes]

  def calculate_fishes(fishes):
    temp = []
    for fish in fishes:
      if fish > 0:
        temp.append(fish - 1)
      if fish == 0:
        temp.append(6)
        temp.append(8)
    return temp

  for i in range(0, 80):
    print("This is day " + str(i))
    lanternfishes = calculate_fishes(lanternfishes)
  print(len(lanternfishes))

def step2():
  file = open("input.txt", "r")
  lanternfishes = file.readline().split(",")
  lanternfishes = [int(i) for i in lanternfishes]
  counter = Counter(lanternfishes)
  for i in range(0, 256):
    new_counter = {}
    for key, amount in counter.items():
      if key > 0:
        if key == 7 and 6 in new_counter:
          new_counter[6] = new_counter[6] + amount
        else:
          new_counter[key-1] = amount
      if key == 0:
        new_counter[8] = amount
        if 6 in new_counter:
          new_counter[6] = new_counter[6] + amount
        else:
          new_counter[6] = amount
    counter = new_counter.copy()

  total = 0
  for key, amount in counter.items():
    total += amount
  print(total)
