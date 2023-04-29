# 15__lists
food = ["Pizza", "Hamburger","Spagetti", "Pudding", "Corn"  ] #lista

food[1] = "Sushi"
print(food[1])

food.append("ice cream") #lägg till
food.remove("Pizza") #ta bort
food.pop(0) #ta bort sista alt värdet alltså plats 0,1,2,3...
food.insert(0, "cake") #lägg till ny på plats
food.sort() #sortera alfabetiskt
# food.clear() #ta bort hela listan

print(food)

list_1 = ["apple", "banana", "cherry"]
list_2 = ("orange", "lemon", "pineapple")            
        

#list fusing
for item_num in range(0, len(list_1)):
    object = list_1[item_num]+list_2[item_num]
    # gör ej mistaget att ha newlist = [] , alltså ny lista som får nytt värde här inne
    # gör ej mistaget att ha en tuple som du försöker lägga in värden i 
    list_1[item_num] = object
print(list_1)