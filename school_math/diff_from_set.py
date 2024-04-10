import numpy as np
import random
import itertools
from collections import Counter
set = np.arange(1,91)
#np.random.seed(37)

def grab_random_elements(set, number=19):
    return np.sort(np.random.choice(set, number, replace=False))

def combine(set):
    return (np.array(list(itertools.combinations(set, 2))))
set19 = grab_random_elements(set)
def diff(set):
    return (set[:,1]-set[:,0])
combined_set = combine(set19)
print(combined_set)
diff_list = (np.sort(diff(combined_set)))
#print(len(diff_list))
print(dict(Counter(diff_list)))
