from PIL import Image
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    inp = int(input("1,2,3: \n"))
except TypeError:
    print("wrong type")


if inp == 1:
# step 1 = create new image by import
    image_name = Image.open("pic.jpg")
    image_name.show()

if inp == 2:
# step 2 = alternative way to import an image
    with Image.open("pic.jpg") as image_name:
        image_name.show

if inp == 3:
    # skapa en ny bild från början
    # Image.new(färg, size)
    image_blank = Image.new("RGB", (1000,600))
    image_blank.show()

