from math import *
import numpy as np
def get_primes(end):
    all = np.arange(2, end+1)
    primes = [2]
    try:
        while True:
            all = all[np.where(all%primes[-1])]
            primes.append(all[0])
    except IndexError:
        return primes
