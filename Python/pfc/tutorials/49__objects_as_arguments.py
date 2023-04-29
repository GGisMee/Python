# 49__objects_as_arguments
# classer är viktiga då de kan användas som storage paket där variablar och annat kan sparas tillsammans och sedan uppkallas. Mest viktigt för organisering och strukturering
from operator import index


class Car:
    color = None


def change_color(car, color): # funkar pga placering då car_1 finns på plats 0 sanmma som car_1
    car.color = color # här får car_1 som i detta fallet beskrivs som car värde röd på .color


car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1, "red")
change_color(car_2, "blue")
change_color(car_3, "black")

print(car_1.color)

