import numpy as np
my_list = ["apples", "banana", "pears", "orange", "fruits"]

# numpy method
# my_list = np.array(["apples", "banana", "pears", "orange", "fruits"])
# my_list = my_list.reshape(-1,1)
# index_list = np.arange(0,len(my_list), 1).reshape(-1,1)

# python way
# for i in range(len(my_list)):
#     my_list[i] = [i,my_list[i]]
# print(my_list)

# smartest way
for i,element in enumerate(my_list):
    my_list.pop(0)
    my_list.append([i,element])
print(my_list)