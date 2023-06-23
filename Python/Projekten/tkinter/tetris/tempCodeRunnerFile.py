from sgl import *
def rotate_from_origo(xy,deg, show=False): # byt kvadrant eller rotera mellansteg
        inherited_k = (Line.points_to_linear_function([0,0], xy)[0])
        inherited_deg = Linear.k_to_degrees(inherited_k)
        deg+=inherited_deg
        length = point(xy).length()
        xy1 = np.array(newcoord.from_deg_xy_len(deg, [0,0], length))
        print(xy1)
        xy1 = np.where(xy1<10**-10,xy1, 0)
        if show:
            print(f"original position: {xy}, inhertited deg: {inherited_deg}")
            print(f"rotation: {deg}, length: {length}")
            print(f"new coord: {xy1}")
        return xy1

rotate_from_origo([-1,0], -90, True)