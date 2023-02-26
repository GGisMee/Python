import numpy as np
import sys

def br():
    print()

# initialisation
a = np.array([1,2,3])
print(a)

b = np.array([[9.0,0.7,6.0],[2.0, 2.3, 4.4]], dtype="int32") 
print(b) # datatyp kan specifisieras för hög effektivitet


# riktningen av arrayen
print(a.ndim)
print(b.ndim)
br()
# storlek av arrayen
print(a.shape)
print(b.shape)
br()
print(a.dtype)
br()
print(a.itemsize)
br()
print(a.size) # hur många bytes
br()
print(a.nbytes) # total storleken
