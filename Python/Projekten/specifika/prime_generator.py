from math import *
import numpy as np
import matplotlib.pyplot as plt
from time import time
end = 100000
def get_primes(end):
    start = time()

    list_of_primes = np.array([3])
    for possible_prime in np.arange(5,end+1,2):
        #print(possible_prime)
        if np.all(possible_prime%list_of_primes):
            list_of_primes = np.append(list_of_primes, possible_prime)
    list_of_primes = np.append(2, list_of_primes)
    print(time()-start)

    plt.plot(np.arange(1,len(list_of_primes)+1), list_of_primes)
    plt.plot(np.arange(1,len(list_of_primes)+1), list_of_primes,"ro",  markersize=10)
    plt.show()

get_primes(end)
