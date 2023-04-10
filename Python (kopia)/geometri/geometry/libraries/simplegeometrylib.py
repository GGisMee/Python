print("simplegeometrylib in use")
import numpy as np
import math
counting_lib_dic = {}
def counting_lib(idholder, variable):
    if idholder not in counting_lib_dic.keys():
        counting_lib_dic.update({idholder:[[0, variable]]})
        return
    if variable not in counting_lib_dic[idholder]:
        counting_lib_dic[idholder].append([len(counting_lib_dic[idholder]), variable]) 

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
    def Linear_point_changer(k=None,m=None,xy=None, show = False):
        if xy[0] == None or xy[0] == None:
            if xy[0] == None:
                xy[0] = (xy[0]-m)/k
            if xy[0] == None:
                xy[0] = k*xy[0]+m
            if show:
                print([xy[0],xy[0]])
            return xy[0],xy[0]
        else:
            if k == None:
                k = (xy[0]-m)/xy[0]
            if m == None:
               m =  xy[0]-k*xy[0]
            if show:
                if m < 0:
                    print(f"xy[0] = {k}x{m}")
                else:
                    print(f"xy[0]={k}x+{m}")
            return k,m
    
    def k_to_degrees(k, show = False):
        degrees = math.degrees(math.atan(k))
        if show:
            print(f"deg={degrees}")
        return degrees
    def change_k_to_degrees(k, degrees, show = False):
        deg=Linear.k_to_degrees(k)
        deg+=degrees
        new_k = math.tan(math.radians(deg))
        if show:
            print(new_k)
        return new_k
    def degrees_to_k(degrees, show = False):
        k = math.tan(math.radians(degrees))
        if show:
            print(k)
        return k

class point:
    def __init__(self, xy):
        self.xy = xy
        counting_lib("point",self)
    def length (self):
        return math.sqrt(self.xy[0]**2+self.xy[1]**2)
