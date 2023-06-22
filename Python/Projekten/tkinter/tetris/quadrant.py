from sgl import *
def rotate_from_origo(xy,deg, show=False): # byt kvadrant eller rotera mellansteg
        try:
            inherited_deg = Linear.k_to_degrees(Line.points_to_linear_function([0,0], xy)[0])
        except ZeroDivisionError:
            # värdet för xy[0] är 0 och därför blir (0-xy[0])/(0-0) zero division error
            #* fixa så den ger ut -90 eller 90, kanske kan man göra så övre istället får k = inf eller k = -inf
            pass
        deg+=inherited_deg
        length = point(xy).length()
        xy1 = newcoord.from_deg_xy_len(deg, [0,0], length)
        if show:
            print(f"original position: {xy}, inhertited deg: {inherited_deg}")
            print(f"rotation: {deg}, length: {length}")
            print(f"new coord: {xy1}")
        return xy1

rotate_from_origo([0,-1], -90, True)