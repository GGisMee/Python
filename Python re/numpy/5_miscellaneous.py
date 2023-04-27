import numpy as np
# från external data
txt = np.genfromtxt("5_data.txt", delimiter=",") # istället för dtype i skapelse V
txt = txt.astype("int16") # räcker för det mesta
print(txt)

# avancerad indexing och boolean maskering
print(txt > 50) # funkar eftersom man kan indexa med en lista V
print(txt[txt > 50]) # tar alla med mer

a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,7]]) # på position 1,2,7
print(a[[False,True,True,False,False,False,False,True, False]]) # på true eller false


print(np.any(txt > 50, axis=0)) # om någon är större än 50
print(np.all(txt > 50, axis = 0)) # om alla är större än 50

print((txt > 50) & (txt < 60)) # tilde gör not 


