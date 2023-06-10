import numpy as np
rows = np.linspace(1,25, 25)
row1 = rows[0:5]
row2 = rows[5:10]
row3 = rows[10:15]
row4 = rows[15:20]
row5 = rows[20:25]
test_data = np.array([row1, row2,row3, row4, row5])
print(test_data)
print(test_data[:,-4:3])
print(test_data[:, 1:3])