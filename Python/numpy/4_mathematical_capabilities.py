import numpy as np
        # matte på listor

def prints(inp):
    print(inp)
    print()
inp = int(input("write: "))
if inp == 0:

    a = np.array([1,2,3,4], dtype="float32")
    a+=2 # simpel matte
    prints(a)
    a/=2 # float krävs för denna
    prints(a)

    b = np.array([1,0,1,0])
    prints(a+b)

    prints(np.sin(a))

        # linjär algebra
elif inp == 1:
     a = np.ones((2,3))
     prints(a)

     b = np.full((3,2), 2)
     prints(b)

     # a*b # funkar ej då olika storlek
     prints(np.matmul(a,b))

     c = np.identity(3)
     prints(np.linalg.det(c))

    # statistik!
elif inp == 2:
    stats = np.array([[1,2,3,], [4,5,6]])
    prints(np.min(stats)) # axis = 1 kan användas för att få för båda små listorna
    prints(np.max(stats))
    prints(np.mean(stats))
    prints(np.median(stats))


    # organizing
elif inp == 3:
    before = np.random.randint(0,10, size=(2,4))
    prints(before)

    after = before.reshape((2,2,2)) # förändra storlek
    prints(after) # krävs samma storlek^

    # stackning
    v1 = np.array([1,2,3,4])
    v2 = np.array([5,6,7,8])
    v_stack = np.vstack([v1,v2])
    prints(v_stack)

    h1 = np.ones((4,4))
    h2 = np.zeros((4,2))

    h_stack = np.hstack([h1,h2])
    prints(h_stack)