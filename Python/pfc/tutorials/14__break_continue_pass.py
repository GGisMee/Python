# 14__break_continue_pass

def de1():
    while True:
        name = input("Enter your name: ")
        if name != "":  # != är samma som not =
            break  # stoppa en loop


def de2():
    telefon_nummer = "072-02-255-25"
    for i in telefon_nummer:
        if i == "-":
            continue
        print(i)


def de3():
    for i in range(1, 100):
        if i == 13:
            pass
        else:
            print(i)


whichpart = input("1,2,3: ")
if whichpart == "1":
    de1()
elif whichpart == "2":
    de2()
else:
    de3()
