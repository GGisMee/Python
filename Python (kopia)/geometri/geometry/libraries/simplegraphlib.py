print("simplegraphlib in use")
#><
import numpy as np
import math
counting_lib_dic = {}
def counting_lib(idholder, variable):
    if idholder not in counting_lib_dic.keys():
        counting_lib_dic.update({idholder:[[0, variable]]})
        return
    if variable not in counting_lib_dic[idholder]:
        counting_lib_dic[idholder].append([len(counting_lib_dic[idholder]), variable]) 

class degrees:
    def shorten_deg(deg, show=False):
        while deg < 0:
            deg+=360
        while deg > 360:
            deg-=360
        if show:
            print(deg)
        return deg


class point:
    def __init__(self, xy):
        self.xy = xy
        counting_lib("point",self)
    def length (self):
        return math.sqrt(self.xy[0]**2+self.xy[1]**2)

class Line:

    def midpoint(xy1,xy2, show=False): # how to ignore required argument when calling a function.
        xymid = [0.5*(xy1[0]+xy2[0]),0.5*(xy1[1]+xy2[1])] # solution (define the argument in the function as a default value, but it can be changed in the calling)
        if show == True:
            print(xymid)
        return xymid

    def points_to_linear_function(xy1, xy2, show=False):
        k_value_var = ((xy1[1]-xy2[1])/(xy1[0]-xy2[0]))
        m_value_var = (xy1[1]-(k_value_var*xy1[0]))
        if show == True:
            tecken = ""
            if m_value_var>=0:
                tecken = "+"
            print(f"y = {k_value_var}x{tecken}{m_value_var}")
        return k_value_var, m_value_var

    # längd i x,y av linje
    def length_between_points(xy1, xy2, show=False):
        xval = abs(xy2[0]-xy1[0])
        yval = abs(xy2[1]-xy1[1])
        if show == True:
            print([xval, yval])
        return xval, yval
    def length_of_line_between_points(xy1, xy2=None, show = False):
        if xy2 != None:
            xlen,ylen = Line.length_between_points(xy1, xy2)
        else:
            xlen = xy1[0]
            ylen = xy1[1]

        hyp = (xlen**2+ylen**2)**(1/2)
        if show:
            print(f"line between is {hyp} steps long")
        return hyp
    
    # prickar på linje
    def line_divider(xy1, xy2,points=1, show=False, outerpoints=False, to_line=False):
        xlen, ylen = Line.length_between_points(xy1,xy2)
        if outerpoints: # skapar värde mellan 0 och 1 som sedan multipliceras med xy1 och adderas med xy1. första sista värdet tas bort 
            xlist = (xy1[0]+xlen*(np.linspace(0,1,points+2))).reshape(-1,1)
            ylist = (xy1[1]+ylen*(np.linspace(0,1,points+2))).reshape(-1,1)
        else: # första sista värdet med 
            xlist = (xy1[0]+xlen*(np.linspace(0,1,points+2))[1:-1]).reshape(-1,1)
            ylist = (xy1[1]+ylen*(np.linspace(0,1,points+2))[1:-1]).reshape(-1,1)

        new_coords = np.hstack((xlist, ylist)) # lägger ihop x och y värdena
        if to_line:
            to_line_list = new_coords[1:]
            new_coords = new_coords[:-1]
            new_coords = np.array(list((zip(new_coords,to_line_list))))
        if show:
            print(new_coords)
        return new_coords

class Linear:
    def Linear_point_changer(k=None,m=None,xy=None, show = False): # tar basically alla förutom 1 och ger tillbaka den saknade
        if xy[1] == None or xy[0] == None:
            if xy[0] == None:
                xy[0] = (xy[1]-m)/k
            if xy[1] == None:
                xy[1] = k*xy[0]+m
            if show:
                print([xy[0],xy[0]])
            return xy[0],xy[1]
        else:
            if k == None:
                k = (xy[1]-m)/xy[0]
            if m == None:
               m =  xy[1]-k*xy[0]
            if show:
                if m < 0:
                    print(f"y = {k}x{m}")
                else:
                    print(f"y={k}x+{m}")
            return k,m
    
    def k_to_degrees(k, show = False): # k värde till grader den är 
        degrees = math.degrees(math.atan(k))
        if show:
            print(f"deg={degrees}")
        return degrees
    def change_k_with_degrees(k, degrees, show = False):
        deg=Linear.k_to_degrees(k)
        deg+=degrees
        new_k = math.tan(math.radians(deg))
        if show:
            print(new_k)
        return new_k
    def degrees_to_k(degrees, show = False): # grader till ett k värde
        k = math.tan(math.radians(degrees))
        if show:
            print(k)
        return k


class newcoord:
    def from_k_xy_x(x, xy, k, show = False): # tar in x värdet för nya punkten, punkten själv och k
        k,m = Linear.Linear_point_changer(k, xy=xy, show=True)
        y = k*x+m
        if show:
            print([x,y])
        return x,y
    def from_deg_xy_len(deg, xy, len, show=False):
        deg = degrees.shorten_deg(deg)
        quadrant_deg = deg
        while deg>90:
            deg-=90

        xchange = len*math.cos(math.radians(deg))
        ychange = len*math.sin(math.radians(deg))

        if 0<quadrant_deg<=90:
            xy = [xy[0]+xchange, xy[1]+ychange]
        if 90<quadrant_deg<=180:
            xy = [xy[0]-ychange, xy[1]+xchange]
        if 180<quadrant_deg<=270:
            xy = [xy[0]-xchange, xy[1]-ychange]
        if 270<quadrant_deg<=360:
            xy = [xy[0]+ychange, xy[1]-xchange]
        if show:
            print(f"change: {[xchange, ychange]}")
            print(f"new coords: {xy}")
        return xy[0], xy[1]



class shape:
    def __init__(self, xy):
        self.xy = np.array([xy])
        counting_lib("shape",self)

    def format(points, length=1, sidelen=True, midpoint=[0,0]): # length är längden av sidorna om sidelen=true, annars är den avstånd från hörn till vinkel
        degrees = 180*(points-2)/points
        if sidelen == True:
            length = length/2/math.cos(math.radians(degrees/2))
        # nu är length säkert avstånd från hörn till vinkel
        new_degrees=0 # för att kunna iterera över ökande grader krävs denna
        for i in range(points):
            if not i:
                new_degrees+=degrees/2
                Linear.change_k_with_degrees(0, new_degrees, True)
            else:
                new_degrees+=degrees
                Linear.change_k_with_degrees(0, new_degrees, True)
        print(degrees,length)
        # implementera kordinater + kalkylerad x+y till varje
