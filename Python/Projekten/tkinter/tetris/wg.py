import numpy as np

print(type(np.array([1,2])))

# class C:
#        def __init__(self, boxes):
#              self.boxes = np.array(boxes)
       
#        def func(self):
#               box_arr = np.resize(np.arange(0, 10*20), (20,10))+1 # ska användas för att genom xy positioner i index få ut boxen att ändra
#               boxes_to_display = np.array(box_arr[:]).T
#               min = np.min(self.boxes[:,0])-1
#               max = np.max(self.boxes[:,0])
#               boxes_to_display = (boxes_to_display[min:max].T)
#               #print(boxes_to_display)
#               boxes_to_display = np.reshape(boxes_to_display, (1, -1))[0]

#               for el1, el2 in self.boxes:
#                      obj = (el1+el2*10)
#                      boxes_to_display = np.delete(boxes_to_display, np.where(boxes_to_display == obj)[0][0])
#               #print(boxes_to_display)
#               for i, el in enumerate(boxes_to_display):
#                      block_area.itemconfig(boxes_to_display, fill="yellow")

       

# c_obj = C([[4,0], [5,0], [6,0],[7,0]])
# c_obj.func()