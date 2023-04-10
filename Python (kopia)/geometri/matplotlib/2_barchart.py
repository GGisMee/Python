from imports import *
plt.figure(figsize=(5,4))
labels = ["A", "B", "C"]
values = [1,4,2]
bars = plt.bar(labels, values)

patterns = ["/", "*", "o"]
for bar in bars:
    bar.set_hatch(patterns.pop(0))

# bars[0].set_hatch("/")
# bars[1].set_hatch("*")
# bars[2].set_hatch("o")

plt.title("Bar")

plt.show()

