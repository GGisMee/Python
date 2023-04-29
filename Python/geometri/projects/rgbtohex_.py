def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'
r = 0
g = 0
b = 0
for i in range(3):
    r += 10
    b += 10
    g += 10
    hex = (rgbtohex(r, g, b))
    print(hex)