# 26__*args
def add(*stuff): # args kan bytas mot vad som hellst som stuff och stuff till args. Dock är stjärnan viktigt för att visa att det är ett argument
    sum = 0
    stuff = list(stuff)
    stuff[0] = 2 # för att ändra ett av valuesen alltså i detta fall blir nummer 0 alltså 1 i värde till 2 i värde
    for i in stuff:
        sum += i
        return sum

print(add(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)) # här läggs 3 värden in, men 2 frågas efter
