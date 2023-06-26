import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Select a snippet of the array
snippet = arr[2:4]

# Perform np.add() operation on the snippet
#snippet+=1
np.add(snippet, 1, out=snippet)

print("Original array:", arr)
print("Updated snippet:", snippet)
