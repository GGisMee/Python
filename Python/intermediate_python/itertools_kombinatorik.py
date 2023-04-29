# tools to handle iteraters ex (lists, tuples, dicts)
from itertools import product
# basically kombinatorik verktyg


# kombinerar ihop i ett multiplikations liknande system
a1 = [1,2]
b1 = [3]
prod = list(product(a1,b1,repeat=2))
# print(prod)


from itertools import permutations
a2 = [1,2,3]
perm = list(permutations(a2, 2)) # 2 visar längd av lista
# print(perm)
# alla ordningar den kan vara i 


from itertools import combinations 
a3 = [1,2,3,4]
comb = combinations(a3, 2)
print(list(comb))
# alla de kan vara ihop med om bara med en annan en gång

