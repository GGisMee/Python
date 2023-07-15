import numpy as np
import matplotlib.pyplot as plt

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
    plt.plot(np.arange(1, len(numbers)+1), numbers)
plt.show()