# 29__random_numbers
import random

x = random.randint(1, 6) # randint står för random interager (nummer som inte innehåller komma)
y = random.random() # helt random nummer under 1
myList = ["rock", "papper", "scissors"]
z = random.choice(myList) # random val utav de som finns
cards = ["ess", 2, 3, 4, 5, 6, 7, 8, 9, "knäckt", "drottning", "kung"]
random.shuffle(cards) # random ordning
print(y, x, z, cards)
