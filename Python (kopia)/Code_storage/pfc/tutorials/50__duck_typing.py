# 50__duck_typing

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwacking")


class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Snake:
    def slither(self):
        print("This snake is slithering")

    def talk(self):
        print("This snake is hissing")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken) # Chicken funkar eftersom den också innehåller walk and talk. Alltså bryr den sig mer om metoderna och attributerna än om Klassen
# person.catch(Snake) # funkar ej då den inte har walk i sig

