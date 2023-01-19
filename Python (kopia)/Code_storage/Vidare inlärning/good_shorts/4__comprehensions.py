
x = []
for i in range(100):
    x.append(0)

print(x, "\n")

y = [0 for i in range(100) if i % 2 == 0] # kompakt sätt att skriva
print(y)
y = [i for i in range(100)]
print(y, "\n")
y = [[0 for i in range(5)] for i in range(5)]
print(y)

sentence = "hello my name is tim"
x = {char: sentence.count(char) for char in set(sentence)}
print(x)