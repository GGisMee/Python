# Python program to create a table
from tkinter import Tk, Frame, Label
import numpy as np
from pandas import DataFrame
if __name__ == "__main__":
	print("This is a tkinter addon which adds the ability to make tkinter Tables")
	exit()

class Table:
	def __init__(self,root, width_height = [7,1]):
		self.labels = []
		self.width_height = width_height
		self.root = root
		self.frame = Frame(root)
		self.frame.pack()

	def populate(self, table_items, fill=False, fill_same=False, id=False, titles=False, font_size = 15):
		self.table_items = np.array(table_items)
		self.row_length = len(self.table_items)
		self.column_length = len(self.table_items[0])
		if titles:
			if not isinstance(table_items,DataFrame):
				print("not pandas DataFrame, therefore usage of titles is denied")
				return
			self.table_items = (np.vstack((table_items.columns.values, self.table_items)))
		if id:
			ids = ((np.arange(self.row_length)+1).reshape((-1,1)))
			if titles:
				ids = np.vstack(("ID", ids))
			self.table_items = np.hstack((ids, self.table_items))
			self.column_length += 1
				
		if fill:
			width = np.amax(np.vectorize(lambda el: len(str(el)))(self.table_items), axis=0)
			for i in range(self.row_length):
				for j in range(self.column_length):		
					self.labels.append(Label(self.frame, width=width[j], height=self.width_height[1], fg='black',
								font=('Arial',font_size,'bold'), text=self.table_items[i][j], highlightbackground="gray", highlightthickness=2))
					self.labels[-1].grid(row=i, column=j)
			self.root.update()
			return
		elif fill_same:
			self.width_height[0] = np.amax(np.vectorize(lambda el: len(str(el)))(self.table_items))
		else:
			self.table_items = np.vectorize(lambda el: str(el)[:self.width_height[0]])(self.table_items)
		for i in range(self.row_length):
			for j in range(self.column_length):			
				self.labels.append(Label(self.frame, width=self.width_height[0], height=self.width_height[1], fg='black',
							font=('Arial',font_size,'bold'), text=self.table_items[i][j], highlightbackground="gray", highlightthickness=2))
				self.labels[-1].grid(row=i, column=j)
