# 46__method_chaining
class Car:
    def turn_on(self):
        print("You started the engine")
        turned_on = "turned on"
        return self
    def turn_off(self):
        print("You turned of the engine")
        return self
    def brake(self):
        print("You stepped on the brake")
        return self
    def drive(self):
        print("You drive the car")
        print("You have previously")
        return self

car = Car()

# Tidigare med två rader
# car.turn_on()
# car.drive()

car.turn_on().drive()

print("-------")

car.brake().turn_off()

print("---------")
car.turn_on().drive().brake().turn_off()

