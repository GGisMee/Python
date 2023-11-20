h=0.001 # approximation of derivative
def f(x):
    return x**2+1

def f_p(x):
    return (f(x+h)-f(x-h))/(2*h)

rate = 1 # between 0<x<2 where 0,...1 is least agressive and 1,99... is most
# 1 to be recommended, however, can be slightly jumpy on an extreme point, then choose 0.1 ex

to_y = 5

def find(start_x,rate=1, max_amount=None, diff=0.001, show=False):
    x = start_x
    i=0
    while abs(to_y-f(x))>diff:
        i+=1
        x += rate*(to_y-f(x))/(f_p(x))
        if i>max_amount:
            break
    if show:
        print(f"x={x}, y(out)={f(x)}, y(in)={to_y}")
    return (x, f(x), to_y, i)
find(start_x=11.4, max_amount=20, show=True)