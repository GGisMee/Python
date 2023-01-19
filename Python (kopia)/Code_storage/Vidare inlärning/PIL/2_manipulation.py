# Rotation, flipping, cropping and scaling aswell as creation of a thumbnail

from PIL import Image
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

image = Image.open("pic.jpg")

if (inp := int(input())) == 1:
    # image rotation                #expand = True för att expandera fottot vid rotering
    rotated_image = image.rotate(10, expand = True) # sker motklocks
    rotated_image.show()

    # andra är
    # fillcolor, för färg i utkant
    # 

if inp == 2:
    pass
else:
    print("error. "+ str(inp))