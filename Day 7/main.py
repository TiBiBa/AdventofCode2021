import numpy as np

def step1():
  file = open("input.txt", "r")
  positions = file.readline().split(",")
  positions = [int(i) for i in positions]
  positions = np.array(positions)

  fuel_usage = {}

  for i in range(min(positions), max(positions)+1):
    fuel = 0
    for position in positions:
      fuel += abs((position - i))
    fuel_usage[i] = fuel

  min_fuel = 9999999999999
  for position, fuel in fuel_usage.items():
    if fuel < min_fuel:
      min_fuel = fuel
  print(min_fuel)

def step2():
  file = open("input.txt", "r")
  positions = file.readline().split(",")
  positions = [int(i) for i in positions]
  positions = np.array(positions)

  fuel_usage = {}

  for i in range(min(positions), max(positions) + 1):
    fuel = 0
    for position in positions:
      fuel += sum(range(1, abs((position - i))+1))
    fuel_usage[i] = fuel

  min_fuel = 9999999999999
  for position, fuel in fuel_usage.items():
    if fuel < min_fuel:
      min_fuel = fuel
  print(min_fuel)
