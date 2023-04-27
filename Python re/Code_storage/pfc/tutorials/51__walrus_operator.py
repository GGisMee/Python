# 51__walrus_operator
# assignment expression. := ser ut som en walrus

happy = True
print(happy)
print()
# hur skriver man detta kombinerat?
# inte så här
# print(happy=True)

# med walrus operators går det:
print(happy := True)

# program:
if 1 == list:
    foods = list()
    while True:
        food = input("What food do you like?:")
        if food.lower() == "quit":
            break
        foods.append(food)
    print(foods)

# implementering
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
print(foods)