import numpy as np
import sys


print(np.zeros((2,3,3))) # kan ge en storlek eller shape
print()
# kan ha 3 diminsioner

print(np.ones((4,2,2))) # kan ge en datatyp på dessa med
print()

print(np.full((2,2), 99)) # kan skriva in vilket nummer som hellst ex 99
print()

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]]) 
print(np.full_like(a,4)) # samma storlek som a, men med 4:or
print()

# random decimaler
print(np.random.rand(4,2))
print(np.random.random_sample(a.shape)) # med a:s storlek
print()

# random interagers
print(np.random.randint(10, 100,size=(2,2))) # mellan 10 och 100
print()
print(np.identity(5)) # längs diagnoalen 1or
print()

# repetitioner
arr = np.array([[1,2,3]]) # måste visa att 2 dimensionell
r1 = np.repeat(arr,3, axis=0) # axis 0 = fler dimensionell
print(r1)
print()

# träning
tr = np.ones((5,5))

z = np.zeros((3,3))
z[1,1] = 9
tr[1:-1,1:-1] = z # går även[1:4]
print(tr)

# var varsam med kopiering av arrays
a = np.array([1,2,3])

# b = a # og förändras
b = a.copy() # bättre kopierings metod!

b[0] = 100
print(a)
print()


