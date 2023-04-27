import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4])
y = np.array([2,4,6,8])

# plt size
plt.figure(figsize=(5,3), dpi=200)
    # dpi = pixel per inch

# ex
# plt.plot(x,y, 
#         label="2x", 
#         color="green", linewidth=3, # hexadecimal färg funkar ocks
#         marker=".", markersize=10, markeredgecolor="blue",
#         linestyle="-" # solid, dashed, dotted, dashdotted
#         )

# shortcut till övre
# ([color][marker][linetype]) alltså r.- 
# vilket är r för red, . för marker, - för en linje
plt.plot(x,y,"r.-",label="2x" )

x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:6:2], x2[:6:2]**2, "bD--", label="x^2")
    # nu visar den bara de första sex
    # visar även en förkortad variation med varannan pga ::2
plt.plot(x2[4::2], x2[4::2]**2, "bD-", label="x^2")


plt.title("Our first graph")
plt.xlabel("x")
plt.ylabel("y")

# kontrollera vilka steg som visas
plt.xticks([0,1,2,3]) # de kommer visas korrekt
plt.yticks([0,2,4,6]) # även om de inte är jämna steg

plt.legend() # lrävs för att visa labeln

# för att spara figuren
plt.savefig("mygraph.png", dpi=300)

plt.show()

