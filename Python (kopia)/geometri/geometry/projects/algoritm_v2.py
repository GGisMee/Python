import matplotlib.pyplot as plt
import time

def converter(totrange,rangestep):
    k = 2.24999999/totrange
    current_amount = k*rangestep-1.999999
    return current_amount


totrange = 1000
listforsave = []
listforc = []
listoferror = []
for i1 in range(totrange):
    c = converter(totrange=totrange, rangestep=i1)
    save = 0
    # save = 0.2

    for i in range(100):
        try:
            save = save**2+c
        except OverflowError:
            listoferror.append(c)
            break
        if i > 50:
            listforsave.append(save)
            listforc.append(c)
print(listoferror)
plt.scatter(listforc, listforsave, s=3)
plt.gca().invert_xaxis()
plt.show()


