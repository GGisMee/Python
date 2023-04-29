# 41__class_variables
from Python.Code_storage.pfc.till_library.Till_41_class_variables import Car
car_1 = Car("Volvo", "V70", 2006, "Black")
car_2 = Car("Fiat", "Multipla", 1997, "light-red")

Car.wheels = 1  # ett sätt att ändra default valuet

car_1.wheels = 2

print(car_1.wheels)
print(car_2.wheels)  # ändras inte då det är default

print(Car.wheels)
