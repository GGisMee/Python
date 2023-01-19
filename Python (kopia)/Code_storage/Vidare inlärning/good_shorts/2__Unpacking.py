tupl = (1, 2, 3, 4, 5)
lst = [1, 2, 3, 4, 5]
string = "hello"
dic = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
coords = [4, 5]

a = tupl[0]
b = tupl[1]
c = tupl[2]
d = tupl[3]
e = tupl[4]
print(a, b, c, d, e)

print()

a, b, c, d, e = tupl  # snyggare sätt
print(a, b, c, d, e)

print()

x,y = coords
print(x, y)