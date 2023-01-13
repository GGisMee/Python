args = [2, 3, 5, 6,7]
print(*args, "\n")
# ett sätt att skriva om from lista till flera variablar

if x := "ja" == "avstängd":
    a,b,c,d = args # denna funkar inte med 7, medan över gör det
    print(a,b,c,d, "\n")

def func1(arg1, arg2, arg3, arg4, arg5):  # auto fördelning
    print(arg1, arg2, arg3, arg4, arg5)


if x := "ja" == "avstängd":
    def func1(*args): # compakt
        print(*args)

func1(*args)