from math import atan, pi
h=0.001
p = 4

def f(x):
    return x**2+1

def fp(f,x):
    return (f(x+h)-f(x-h))/(2*h)

def find(p,f,rate, min:bool):
    'Find min or max of func: f with point p as start x value with a rate of change of rate'
    minmax = -1 if min==True else 1
    cap = 2000
    i=0
    while i<cap:
        i+=1
        change = rate*minmax*2/pi*(atan(fp(f,p)))
        p+=change
        if abs(f(p)-f(p-change))<0.001:
            break
    print(p)

find(p,f,1,1)
