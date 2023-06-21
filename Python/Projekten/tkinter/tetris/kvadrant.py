import sgl
inp = [1,1]
dgr = 90
inherited_dgr = sgl.Linear.k_to_degrees(sgl.Line.points_to_linear_function([0,0], inp)[0])
print((sgl.point(inp)))
dgr+=inherited_dgr
len = sgl.point.length(inp)
sgl.newcoord.from_deg_xy_len(dgr, [0,0], len, show=True)
