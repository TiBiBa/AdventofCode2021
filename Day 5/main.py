from collections import Counter

file = open("input.txt", "r")
vents = file.read().splitlines()
points = []

def step1():
  for vent in vents:
    coordinates = vent.split('->')
    x1 = int(coordinates[0].split(',')[0])
    y1 = int(coordinates[0].split(',')[1])
    x2 = int(coordinates[1].split(',')[0])
    y2 = int(coordinates[1].split(',')[1])
    if not (x1 != x2 and y1 != y2):
      if x1 < x2:
        for i in range(x1, x2+1):
          points.append((i, y1))
      elif x1 > x2:
        for i in range(x2, x1+1):
          points.append((i, y1))
      elif y1 < y2:
        for i in range(y1, y2+1):
          points.append((x1, i))
      elif y1 > y2:
         for i in range(y2, y1+1):
           points.append((x1, i))

  c = Counter(points)
  counter = 0
  for point, count in c.items():
    if count >= 2:
      counter += 1
  print(counter)

def step2():
  points = []
  for vent in vents:
    coordinates = vent.split('->')
    x1 = int(coordinates[0].split(',')[0])
    y1 = int(coordinates[0].split(',')[1])
    x2 = int(coordinates[1].split(',')[0])
    y2 = int(coordinates[1].split(',')[1])
    if not (x1 != x2 and y1 != y2):
      if x1 < x2:
        for i in range(x1, x2 + 1):
          points.append((i, y1))
      elif x1 > x2:
        for i in range(x2, x1 + 1):
          points.append((i, y1))
      elif y1 < y2:
        for i in range(y1, y2 + 1):
          points.append((x1, i))
      elif y1 > y2:
        for i in range(y2, y1 + 1):
          points.append((x1, i))
    else:
      counter = 0
      if (x1 < x2 and y1 < y2):
        for i in range(x1, x2+1):
          points.append((i, y1+counter))
          counter += 1
      elif (x1 > x2 and y1 > y2):
        for i in range(x1, x2-1, -1):
          points.append((i, y1-counter))
          counter += 1
      elif (x1 > x2 and y1 < y2):
        for i in range(x1, x2-1, -1):
          points.append((i, y1+counter))
          counter += 1
      elif (x1 < x2 and y1 > y2):
        for i in range(x1, x2+1):
          points.append((i, y1-counter))
          counter += 1

  c = Counter(points)
  counter = 0
  for point, count in c.items():
    if count >= 2:
      counter += 1
  print(counter)

