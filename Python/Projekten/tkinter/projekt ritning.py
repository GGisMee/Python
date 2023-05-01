
input1 = input("1,2,3 alltså  1 för hörnfigur, 2 för snöflinga, 3 för Flingor i färg och randomiserat: ")
if int(input1) == 1:
    from turtle import *
    color("blue")
    shape("turtle")
    pensize(5)
    horn = input("Vilken figur? 3,4,5,6,7,8,9 hörn ?:")
    rangen = int(horn) + 1
    right_hoger = 360 / int(horn)
    speed(int(horn) - 2)
    till_forwardness = float(horn) / 10
    for x in range(1, rangen):
        forward(50 / float(till_forwardness))
        right(right_hoger)

    hideturtle()
    input()
elif int(input1) == 2:
    from turtle import *
    pencolor("white")
    Screen().bgcolor("turquoise")
    speed(30)

    def vform():
        right(25)
        forward(50)
        backward(50)
        left(50)
        forward(50)
        backward(50)
        right(25)

    def snoflingearm():
        for x in range(0, 4):
            forward(30)
            vform()
        backward(120)

    flakes = int(input("amount of flakes here: "))

    def snoflinga():
        for x in range(0, flakes):
            snoflingearm()
            right(360 / flakes)
    snoflinga()
    input()


else:
    stor1 = input("antal storlek, mm: ")
    stor = float(stor1)
    import random
    from turtle import *

    pencolor("white")
    farger = ("blue", "yellow", "purple", "cyan", "green", "orange", "red")
    Screen().bgcolor("black")
    speed(3000)


    def vform(stor):
        right(25)
        forward(stor)
        backward(stor)
        left(50)
        forward(stor)
        backward(stor)
        right(25)


    def snoflingearm(stor):
        for x in range(0, 4):
            forward(stor)
            vform(stor)
        backward(stor * 4)



    def snoflinga(stor):
        for x in range(0, 6):
            color(random.choice(farger))
            snoflingearm(stor)
            right(60)

    for i in range(0, 10):
        size = random.randint(5, 30)
        x = random.randint(-400, 400) # random interval alltså max: a, min: b
        y = random.randint(-400, 400)
        penup()
        goto(x, y)
        pendown()
        snoflinga(stor)
    input()

