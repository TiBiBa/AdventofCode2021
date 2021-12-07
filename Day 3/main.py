import pandas as pd

file = open("input.txt", "r")
binaries = file.readlines()

def binaryToDecimal(binary):
  binary1 = binary
  decimal, i, n = 0, 0, 0
  while (binary != 0):
    dec = binary % 10
    decimal = decimal + dec * pow(2, i)
    binary = binary // 10
    i += 1
  return decimal

#step 1
gamma = ""
epsilon = ""
for i in range(0, len(binaries[0])-1):
    current_step_0 = 0
    current_step_1 = 0
    for binary in binaries:
      if binary[i] == '0':
        current_step_0 += 1
      else:
        current_step_1 += 1
    if current_step_0 > current_step_1:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
gamma = binaryToDecimal(int(gamma))
epsilon = binaryToDecimal(int(epsilon))
print(gamma * epsilon)

print("****************************************")

#step 2
df = pd.read_csv("input.txt", dtype=object, names=['binary'])
df = df['binary'].str.split('', expand=True)
df = df.iloc[:, 1:]
df = df.iloc[:, :-1]
df.apply(pd.to_numeric)

oxygen = None
coTwo = None

df_oxygen = df.copy()
df_coTwo = df.copy()

for name, values in df_oxygen.iteritems():
    amount_one = df_oxygen[name].value_counts()['1']
    amount_zero = df_oxygen[name].value_counts()['0']
    delete_number = 0
    if amount_one < amount_zero:
        delete_number = 1
    df_oxygen = df_oxygen.drop(df_oxygen[df_oxygen[name] == str(delete_number)].index)
    if df_oxygen.shape[0] == 1:
        oxygen = df_oxygen.values.tolist()
        break

for name, values in df_coTwo.iteritems():
    amount_one = df_coTwo[name].value_counts()['1']
    amount_zero = df_coTwo[name].value_counts()['0']
    delete_number = 1
    if amount_one < amount_zero:
        delete_number = 0
    df_coTwo = df_coTwo.drop(df_coTwo[df_coTwo[name] == str(delete_number)].index)
    if df_coTwo.shape[0] == 1:
        coTwo = df_coTwo.values.tolist()
        break

temp = ""
for number in oxygen[0]:
  temp += number
oxygen = int(temp)
temp = ""
for number in coTwo[0]:
  temp += number
coTwo = int(temp)

print(oxygen)
print(coTwo)

oxygen = binaryToDecimal(int(oxygen))
coTwo = binaryToDecimal(int(coTwo))
print(oxygen * coTwo)
