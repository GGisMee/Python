from collections import Counter
string = "aaaaaaaabbbbbbcccc"

counted = Counter(string)
print(list(counted.values()))