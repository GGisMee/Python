# Python program to create a table
from tkinter import *
import numpy as np

class Table:
	def __init__(self,root, width_height = [7,1]):
		self.labels = []
		self.width_height = width_height
		self.frame = Frame(root)
		self.frame.pack()

	def populate(self, table_items, fill=False, fill_same = False):
		self.table_items = np.array(table_items)
		self.row_length = len(self.table_items)
		self.column_length = len(self.table_items[0])
		
		#np.vectorize(lambda el: print(el))(self.table_items)
		if fill:
			width = np.amax(np.vectorize(lambda el: len(str(el)))(self.table_items), axis=0)
			for i in range(self.row_length):
				for j in range(self.column_length):			
					self.labels.append(Label(self.frame, width=width[j], height=self.width_height[1], fg='black',
								font=('Arial',16,'bold'), text=self.table_items[i][j], highlightbackground="gray", highlightthickness=2))
					self.labels[-1].grid(row=i, column=j)
		elif fill_same:
			self.width_height[0] = (np.amax(np.vectorize(lambda el: len(str(el)))(self.table_items)))
		else:
			self.table_items = np.vectorize(lambda el: str(el)[:self.width_height[0]])(self.table_items)
		for i in range(self.row_length):
			for j in range(self.column_length):			
				self.labels.append(Label(self.frame, width=self.width_height[0], height=self.width_height[1], fg='black',
							font=('Arial',16,'bold'), text=self.table_items[i][j], highlightbackground="gray", highlightthickness=2))
				self.labels[-1].grid(row=i, column=j)

