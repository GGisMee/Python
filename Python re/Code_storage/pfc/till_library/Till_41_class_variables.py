class Car:

    wheels = 4  # class variabel. Som ett defualt value som står för alla sorter i detta fallet car_1 och car_2

    def __init__(self, make, model, year, colour):
        self.make = make # dessa heter instance variables
        self.model = model
        self.year = year
        self.colour = colour