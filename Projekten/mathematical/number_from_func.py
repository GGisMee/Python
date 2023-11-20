import sympy as sp
num = 20
#int(input('ins num'))
towards = 0
method = False # True means number of iterations, False equals to a certain proximity

def mf(x): # mf for mathematical function, där f'>0
    return x**5+x-1

iterations = 10
proximity = 0.001

changing_factor = num/2
changed_direction = False

direction = 1 if mf(num)<towards else 0
while_iterations = 0
while changed_direction == False:
    while_iterations +=1
    num = num + direction*changing_factor - (not direction)*changing_factor

    if (not direction and mf(num)<towards or direction and mf(num)>towards):
        break
    changing_factor*=2

for i in range(iterations):
    changing_factor/=2
    if mf(num)<towards:
        num+=changing_factor
    else:
        num-=changing_factor
print(num,mf(num), changing_factor)
