import numpy as np
import pandas as pd
tal = int(input('Enter number: '))
list_of_used_primes = [0]

def get_primes(end):
    all = np.arange(2, end+1)
    primes = [2]
    try:
        while True:
            all = all[np.where(all%primes[-1])]
            primes.append(all[0])
    except IndexError:
        return primes

primes = np.array(get_primes(tal/2))
while tal != 1:
    used_primes = (primes[np.logical_not(tal%primes)].astype(int))
    list_of_used_primes = np.append(list_of_used_primes,used_primes)
    tal/=np.prod(used_primes)
    #print(tal)
list_of_used_primes = list_of_used_primes[1:]
print(list_of_used_primes)
primes_dict = {}
print_str = ""
for prime_num in np.unique(list_of_used_primes):
    length_of_prime_num = str(len(list_of_used_primes[list_of_used_primes == prime_num]))
    primes_dict[str(prime_num)] = length_of_prime_num

    if length_of_prime_num == "1":
        print_str+=f"{prime_num} "
        continue
    print_str+=f"{prime_num}^{length_of_prime_num} "
print(print_str[:-1])
# fixa dessa som en loop
