import numpy as np
from math import log10
def input_f():
    try:
        return int(input("Enter number: "))
    except ValueError:
        input_f()
#decimal = input_f()

def binary_to_decimal(binary):
    print(len(binary))
    all_pow_2 = (np.flip(2**np.arange(0,int(log10(2**len(binary))/log10(2)))))
    decimal = np.sum(all_pow_2[binary.astype(bool)])
    return decimal

    
def decimal_to_binary(decimal):
    pow_2 = []
    i=1
    while decimal != 0:
        while decimal >= i:
            i*=2
        else:
            pow_2.append(int(i/2))
            decimal-=int(i/2)
            i=1
    all_pow_2 = (np.flip(2**np.arange(0,int(log10(np.max(pow_2))/log10(2))+1)))
    binary = (np.isin(all_pow_2,pow_2).astype(int))
    return binary
binary = decimal_to_binary(7)


# y = 2^x
# log y / log 2