import numpy as np
import matplotlib.pyplot as plt
ax = plt.figure().add_subplot(projection='3d')
def get_conjecture(number):
    numbers = [number]
    while number != 1:
        number = (number/2*(not number%2)+(number*3+1)*(number%2))
        numbers.append(number)
    return numbers, len(numbers)
def input_f():
    try:
        return int(input("Enter number: "))
    except ValueError:
        input_f()

for i in range(2, 101):
    numbers = get_conjecture(i)[0]
    ax.plot(np.arange(1, len(numbers)+1), numbers, zs=i, zdir='z', label='curve in (x, y)')
ax.view_init(elev=145, azim=-20, roll=90)
plt.show()