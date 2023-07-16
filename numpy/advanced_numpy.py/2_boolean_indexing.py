import numpy as np
rows = np.linspace(1,25, 25)
row1 = rows[0:5]
row2 = rows[5:10]
row3 = rows[10:15]
row4 = rows[15:20]
row5 = rows[20:25]

greater_than_five = rows > 5
# print(greater_than_five)
# print(rows[greater_than_five])

# where method
drop_under_5_array = np.where(rows > 5, rows, 0)
# argument, true value, false value
# print(drop_under_5_array)

# logical_and
drop_under_5_and_20 = np.logical_and(rows >5, rows<20)
print(rows[drop_under_5_and_20]) # använder en or gate på kartan