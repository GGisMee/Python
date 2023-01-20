# Rotation, flipping, cropping and scaling aswell as creation of a thumbnail

from PIL import Image, ImageColor
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

image = Image.open("pic.jpg")
inp = int(input())
if inp == 1:
    # image rotation                #expand = True för att expandera fottot vid rotering
    rotated_image = image.rotate(10, expand = True, fillcolor= ImageColor.getcolor("red", "RGB")) # sker motklocks
    rotated_image.show()                                # tar emot rgb

    # andra är
    # fillcolor, för färg i utkant      # fillcolor= (255, 0, 50))      ImageColor.getcolor("red", "RGB")
    # center var som rotaitoner roterar ifrån  
elif inp == 2:
    # ta en del av bilden
    croped_image = image.crop((200,200, 400, 300)) # (x1, y1, x2, y2)
    croped_image.show()

elif inp == 3:
    # flippa bilden 
    image_flip_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    image_flip_horizontal = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    image_flip_horizontal = image.transpose(Image.Transpose.TRANSPOSE)
    image_flip_horizontal.show()

elif inp == 4:
    # image resize
    resized_image = image.resize((600,1000)) # simple version

    scale_factor = 0.5
    resized_image = image.resize((int(float(image.size[0])*scale_factor), int(float(image.size[1])*scale_factor)))
    resized_image.show()
else: 
    print("error. "+ str(inp))