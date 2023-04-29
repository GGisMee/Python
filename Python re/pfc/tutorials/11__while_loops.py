# 11__while_loops
# while 1==1:
#   print("lol")

# del 2 version 1.1 och 1.2
namn = ""

while namn == "":  # alternativt längden på namnet alltså while len(namn) == 0:
    namn = input("What is your name: ")
while not namn == "":  # för att se till att något inmatas!
    print("noice")

print("Hej " + namn)  # alt lösning utanför while kretsen

# version 2
# namn = None

# while not namn:
#   namn = input("What is your name: ")
#
# print("Hej "+namn) #alt lösning utanför while kretsen
