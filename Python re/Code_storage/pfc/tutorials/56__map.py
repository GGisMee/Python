# 56__map
# gör en funktion på varje sak i en samling(lista, tuple, etc)
# skrivs map(funktionnamn, samling)
inp = int(input("Ex: \n 1 (Bro Code) \n 2 (w3schools)\nWrite here: "))

if inp == 1:
    store = [
        ("t-shirt", 20.00), 
        ("pants", 25.00), 
        ("jacket", 50.00), 
        ("socks", 10.00)
    ]

    to_sek = lambda currency: (currency[0], currency[1]*10.9)
    to_dollar = lambda currency: (currency[0], currency[1]/10.9)

    store_sek = list(map(to_sek, store))

    store_dollar = list(map(to_dollar, store))

    print(store_sek)
    print()
    print(store_dollar)

else:
    inp = int(input("Ex:  \n1: \n2: \nWrite here: "))
    
    if inp == 1:
        myfunc = lambda a: len(a)
        x = map(myfunc, ("apple", "banana", "cherry"))
        print(x)
        print(list(x))

    if inp == 2:
        myfunc = lambda a,b: a+b
        x = map(myfunc, ("apple", "banana", "cherry"), ("orange", "lemon", "pineapple"))
        # här går den direkt in i varje objekt och ändrar
        print(x)
        print(list(x)) 
        print()

        list_1 = ["apple", "banana", "cherry"]
        list_2 = ("orange", "lemon", "pineapple")            

        # här måste man gå in djupare 
        for item_num in range(0, len(list_1)):
            object = list_1[item_num]+list_2[item_num]
            # gör ej mistaget att ha newlist = [] här inne
            # gör ej mistaget att ha en tuple som du försöker lägga in värden i 
            list_1[item_num] = object
        print(list_1)