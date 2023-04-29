# 40__Object_Oriented_Programming_OOP
# Detta är objekt som man kan göra i verkligheten. T.ex. kan detta vara något i ens närhet som telefon, Dator, Fönster, Bok, Laddare, Bord mm
# en klass förklarar vad ett objekt handlar om
from Python.Code_storage.pfc.till_library.Till_40_OOP_Car import Car # man kan tyvärr bara välja i foldrar som finns i samma sida. genom att skriva punkterat
car_1 = Car("Volvo", "V70", 2006, "Black")
car_2 = Car("Fiat", "Multipla", 1997, "light-red")

which_car = car_2
print(which_car.make)
print(which_car.model)
print(car_2.year)
print(car_2.colour)

print()
which_car.drive()
which_car.stop()
