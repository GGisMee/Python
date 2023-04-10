from imports import *

x = np.array([0,1,2,3,4])
y = 2*x

# scale of figure (bakgrunden)
# dpi är pixlar per inch, basically storlek på figure
plt.figure(figsize=(5,3), dpi=50)


# plt.plot(x,y, label="x^2", color="green", linewidth=2, marker=".", markersize=6, linestyle="-")
    # linestyles: --  -  -.  :
    # markers: . ^ * o
    # colors: alla

# shorthand
# format = [color][marker][line]
plt.plot(x,y, "ro:",  label="x^2")

plt.title("Simple Graph", fontdict={"fontname":"Comic Sans MS", "fontsize":20})
plt.xlabel("x") # fontdict funkar för dessa med
plt.ylabel("y")

# displayed numbers on side, finns dock auto bra
plt.xticks(np.linspace(np.min(x),np.max(x),len(x)))
plt.yticks(np.linspace(np.min(y),np.max(y),len(y)))

plt.legend()


# en linje med specielare värden
x2 = np.arange(0,4, 0.5)
plt.plot(x2[:4],x2[:4]**2, "y--")
plt.plot(x2[3:],x2[3:]**2, "g-")

# sparar bilden
plt.savefig("mygraph.png", dpi=300)

plt.show()