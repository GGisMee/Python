from simplegeometrylib import *
from tkinter import *
p1 = [0,0]
p2 = [1,1]
p3 = Line.midpoint(p1, p2 ,show=True)
k = Line.points_to_linear_function(p1, p2, show=False)[0]
new_k = Linear.change_k_to_degrees(k,90, show=False)
degrees = abs(Linear.k_to_degrees(new_k, show=True))

hyp = Line.length_of_line_between_points(p3,show=True)

xlen = hyp*math.tan(math.radians(degrees))+p3[0]
ylen = hyp*abs(math.sin(math.radians(degrees)))+p3[1]
print(xlen, ylen)

p1 *= 100
p2*= 100


window = Tk()
canvas = Canvas(window, width=200, height=200)
canvas.pack()


window.mainloop()



# mid = 0.5 0.5
