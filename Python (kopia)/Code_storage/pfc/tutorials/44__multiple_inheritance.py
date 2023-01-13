# 44__multiple_inheritance
# when a child has more than one parent
class Pray():
    def flee(self):
        print("This animal Flees")


class Predator():
    def hunt(self):
        print("This animal hunts")


class Rabbit(Pray):
    pass


class Hawk(Predator):
    pass


class Zebra(Pray):
    pass


class Fish(Pray, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
zebra = Zebra()
fish = Fish()

print("The rabbit:")
rabbit.flee()
print("---------------------\n"
      "The hawk:")
hawk.hunt()
print("---------------------\n"
      "The fish:")
fish.hunt(), fish.flee()
print("---------------------\n"
      "The zebra:")
try:
    print(zebra.hunt())
except AttributeError:
    print("This animal can't hunt, because it doesn't have the parent that it can inherite that from!")