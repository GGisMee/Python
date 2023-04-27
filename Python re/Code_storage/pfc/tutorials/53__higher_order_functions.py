# 53__higher_order_functions
# funktioner är lika påverkade som objekt
"""
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func, inp):
    text = func(inp) # nästan som nested då en funktion förklarar en annan funktion
    print(text)

inp = input("Write text here: ")
hello(loud, inp)
"""

# ex 2
def nämnarF(nämnarV): # sus att täljarF kallas, men börjar ytterst och skalar sen in därför först 2 och sedan 10
    def täljarF(täljarV):
        return täljarV/nämnarV
    return täljarF


dela = nämnarF(2)
print(dela(10))