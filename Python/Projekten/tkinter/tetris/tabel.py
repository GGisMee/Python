# Python program to create a table

from tkinter import *
import pandas as pd


lst = [(1,'Raj','Mumbai',19),
	(2,'Aaryan','Pune',18),
	(3,'Vaishnavi','Mumbai',20),
	(4,'Rachna','Mumbai',21),
	(5,'Shubham','Delhi',21)]


class Table:
	
	def __init__(self,root, ):
		
		# code for creating table
		for i in range(total_rows):
			for j in range(total_columns):
				
				self.label = Label(root, width=20, fg='black',
							font=('Arial',16,'bold'), text=lst[i][j], highlightbackground="gray", highlightthickness=2)
				
				self.label.grid(row=i, column=j)
				#self.e.insert(END, lst[i][j])

# take the data


# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()
