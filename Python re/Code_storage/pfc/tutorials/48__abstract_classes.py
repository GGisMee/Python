# 48__abstract_classes

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod # detta och ABC över i class gör att man inte kan kalla denna klassen då den bara kan ge ut sin info
    def go(self): # kan likna en constant i js
        pass

    @abstractmethod # abstrakta metoder kan skrivas över en funktion.
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("you stopped the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("you stopped this motorcycle")

class Bicycle(Vehicle):
    pass

    def stop(self):
        print("you hit the break")

car = Car()
motorcycle = Motorcycle()
# bicycle = Bicycle()  # abstrakta metoder kan även användas för att kräva att en child class har overridat en funktion

# vehicle = Vehicle()

car.go()
motorcycle.go()
# bicycle.go()
# vehicle.go()

