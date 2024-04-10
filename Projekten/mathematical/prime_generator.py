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

primes200 = get_primes(200)
print(primes200, len(primes200))
new_primes = []
length = 0
for prime in primes200:
    inner_new_primes = []
    for prime2 in primes200:
        if prime*prime2 > 200:
            primes200 = primes200[1:]
            break
        inner_new_primes.append(prime2)
    new_primes.append(inner_new_primes)
    length += len(inner_new_primes)
print(new_primes ,length)