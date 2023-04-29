# 57__filter
# skapar ett sammanhang av element från en sammling, vilket en funktion ger tillbaka
betweening = print

friends = [
    ("Noah", 19), # name and age
    ("William", 18),
    ("Axel", 17),
    ("Ludwig", 16),
    ("Allie", 21),
    ("Nils", 20)
]

# without filters
for friend in friends:
    if friend[1] >= 18:
        print(friend[0])
    else:
        pass

betweening()

# with filters
age = lambda position: position[1] >= 18 # ger tillbaka de som har värdet sant då filter

oldness = list(filter(age, friends))
oldnessness = list(map(age, friends)) # ger ej tillbaka items, utan värden
print(oldnessness)
betweening()

check = lambda checking: checking[0]
oldness = map(check, oldness)
print(list(oldness))