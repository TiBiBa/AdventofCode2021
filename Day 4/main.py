import numpy as np

numbers = open("input.txt", "r").readline().split(",")
numbers = [int(i) for i in numbers]

#step 1
def step1():
  bingo_cards = np.genfromtxt('input.txt', skip_header=2)
  found = False
  for number in numbers:
    if found:
      break
    bingo_cards[bingo_cards == number] = -1
    for i in range(0, len(bingo_cards), 5):
      if found:
        break
      bingo_card = bingo_cards[i:i+5]
      if -5 in np.sum(bingo_card,axis=1).tolist() or -5 in np.sum(bingo_card, axis=0).tolist():
        print("bingo!")
        total = np.sum(bingo_card, where=bingo_card > 0)
        print("The last number was... " + str(number))
        print("The answer is.... " + str(number * total))
        found = True

#step 2
def step2():
  bingo_cards = np.genfromtxt('input.txt', skip_header=2)
  for number in numbers:
    bingo_cards[bingo_cards == number] = -1
    for i in range(0, len(bingo_cards), 5):
      bingo_card = bingo_cards[i:i+5]
      if -5 in np.sum(bingo_card,axis=1).tolist() or -5 in np.sum(bingo_card, axis=0).tolist():
        if len(bingo_cards) <= 5: #there is only one card left
          print("last bingo!!")
          total = np.sum(bingo_card, where=bingo_card > 0)
          print("The last number was... " + str(number))
          print("The answer is.... " + str(number * total))
        bingo_cards = np.delete(bingo_cards, ([i, i+1, i+2, i+3, i+4]), axis=0)
