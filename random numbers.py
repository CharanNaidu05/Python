import random 

#number = random.randint(1, 6)
#print(number)

low = 1
high = 100

#number = random.randint(low, high)
#print(number)

#number = random.random() #For floating point
#print(number)

#options = ("rock", "papper", "scissors")
#option = random.choice(options)
#print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)