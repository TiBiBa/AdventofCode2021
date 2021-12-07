file = open("input.txt", "r")
measurements = file.read().split()
measurements = [int(i) for i in measurements]

#step 1
counter = 0
for i in range(1, len(measurements)):
  if measurements[i] > measurements[i-1]:
    counter += 1
print(counter)

print("****************************************")

#step 2
counter = 0
window = 99999
for i in range(0, len(measurements)-2):
    temp = measurements[i] + measurements[i+1] + measurements[i+2]
    if temp > window:
        counter += 1
    window = temp
print(counter)

