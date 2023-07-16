import numpy as np
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]]) # båda arraysen måste dumt nog vara lika stora
print(a)
print()
# för att få ut ett specifikt värde kan man tänka rader och kolumner
# alltså (r,c) från 0 som vanligt
print(a[0,4])
print(a[1,-2]) # negativa funkar även
print()
# specifik rad
print(a[0,:])
print(a[:,0]) # : för alla
print()

# mixtrande
print(a[0,1:6:2])
print()

# förändra värden
a[0,3] = 5 # byter ett specifikt värde
a[:,0] = [0,7] # byter i kolumn
print(a)
print()

# 3d array
b = np.array([[[1,2],[3,4]],[[5,6], [7,8]]])
print(b[0,1,1]) # tips printa först välj sen
b[:,1,1] = [2,1]
print(b[:,1])