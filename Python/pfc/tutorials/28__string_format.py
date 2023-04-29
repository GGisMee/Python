# 28__string_format
animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item) # metod 1
print("The {} jumped over the {}".format(animal, item)) # alternativt strings i format delen
print("The {1} jumped over the {0}".format(animal, item)) # positional argument
print("The {item} jumped over the {animal}".format(animal="cow", item="moon"))  # keyword argument
# man kan på båda dessa över skriva ned 2 av samma value och nyckel eller variabel i båda måsvingarna {}

text = "The {} jumped over the {}"
print(text.format(animal, item))

print("------------------------------------------------------------")

name = "Gustav Gamstedt"
print("Hello, my name is {:20}. Nice to meet you".format(name))
print("Hello, my name is {:<20}. Nice to meet you".format(name)) # höger sida
print("Hello, my name is {:>20}. Nice to meet you".format(name)) # vänster sida  <>
print("Hello, my name is {:^20}. Nice to meet you".format(name)) # båda sidor
print("------------------------------------------------------------")
number = 1003.14159

print("The number pi is {:.2f}".format(number)) # här avrundas det med (:."avrundningsnummer"f) där "avrundningsnummer" är numret som ska avrundas i detta fall på plats 2: 4
roundness = round(3.1415,2) # här avrundar jag med round(variabelnummer, roundnummer) där roundnummer är platsen som det avrundas från i detta fallet på plats 2 alltså avrundas fyran
print(roundness)
roundness = 3.1415.__round__(2) #  ennu en alternativ metod för avrundning men nu med __round__(avrundningsnummer) där avrundningsnummret i detta fallet är på plats 2 alltså avrundas fyran
print(roundness)

print("------------------------------------------------------------")

# avrundning och annan taluppsättning
print("The number pi is {:,}".format(number))  # lägger till , på varje 10^3 platsen
print("The number pi is {:b}".format(int(number)))  # denna gör koden i binär
print("The number pi is {:o}".format(int(number)))  # detta gör koden i 8 tal
print("The number pi is {:X}".format(int(number)))  # skum beskrivning, men kort och simpel
print("The number pi is {:E}".format(int(number)))  # E metoden för stora tal
print("------------------------------------------------------------")
tal = 1003.123
tal = "{:b}".format(int(tal)) # annat sätt att skriva och ändra utan print
print(tal)
