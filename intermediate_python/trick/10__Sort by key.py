# sortera i en unik ordning
lst = [[1, 2], [3, 4], [4, 2], [-1, 3], [4, 5], [2, 3]]
lst.sort()
print(lst)  # detta sorterar av första elementet i inre listan

def sort_func(x):
    return x[0] + x[1] # sortering funktion

lst.sort(key=sort_func)
print(lst)