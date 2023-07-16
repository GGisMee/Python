# 54__lambda
# är en funktion som är skriven i en rad
# lambda innehåll:förändring
nr = int(input("Write num here. method(1,2)"))
if nr == 1:
    def double(x): # här är x innehåll utifrån
        return (x*2) # här är förändringen

    print(double(5))

if nr == 2:
    doubeling = lambda x: x*2 # liknar arrow func
    multiply = lambda x, y: x*y
    add = lambda x,y,z: x+y+z
    full_name = lambda first_name, last_name: f"{first_name} {last_name}" # first_name + " " + last_name, funkar också
    age_check = lambda age:True if age >= 18 else False
    # ovan skrivs return före if statementet, else med return efter 

    print (f"double: {doubeling(5)}")
    print(f"multiply: {multiply(5,4)}")
    print(f"add: {add(4,5,7)}")
    print(full_name("Gustav", "Gamstedt"))
    print(age_check(18)) 

    # användbart för korta funktioner som inte kräver flera rader, samt för små funktioner som bara används någon gång
    