# 52__functions_to_variables
def hello():
    print("Hello")


hello()  # ett sätt att kalla funktionen
print()

print(hello)  # detta är en plats där hello finns som visas när man inte skriver in funktionens paranteser
# man kan tänka att det är en adress till ett hus som djäknegatan 14

print()

hi = hello  # detta gör som om hello också kan kallas med hi
hi()  # nu när de har samma adress så kommer hi kalla hello funktionen

print("-------------------------------------------------------")

say = print("Wow i can't believe this works")
say  # här kallar say på print