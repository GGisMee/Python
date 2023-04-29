# 42__inheritance
# att få från tidiagere alltså kan child få allt som parent ger
class Animal:  # För att kompaktera delad fakta till en
    alive = True

    def eat(self):
        print("This animal need to eat to survive")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):  # här får Rabbit all kod från Animal då den är i paranteserna
    def run(self):
        print("Im runnning as fast as Usain Bolt!!!!!!! and im running")


class Hawk(Animal):
    def Fly(self):
        print("I'm Flying like an rc plane and im a Hawk")


class Fish(Animal):  # dessa är alltså Parent: Animal's tre Children.
    def swim(self):
        print("Im swimming fastly and i am a Fish")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()
print(Rabbit.alive)  # även om det inte står något i Rabbit class så får den inheritance från Animal
rabbit.eat(), rabbit.run()
hawk.Fly(), fish.swim()