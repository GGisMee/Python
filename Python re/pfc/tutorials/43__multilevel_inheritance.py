# 43__multilevel_inheritance

class Organism:  # grandparent

    alive = True


class Animal(Organism):  # parent
    def eat(self):
        print("This animal is eating!")


class Dog(Animal):  # child
    def bark(self):
        print("This dog is barking")


class Door():
    def Creak(self):
        print("This door creaks!")

dog = Dog()
if dog.alive:  # här så ärver Dog från 2 steg bakåt i organism
    print("This dog is an organism")
dog.eat()
dog.bark()
