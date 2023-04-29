from PIL import Image
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    inp = int(input("[...]: \n"))
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

if inp == 4:
    image_name = Image.open("pic.jpg")

    # spara som namnet...
    image_name.save("save.png") # val över vilken typ
                                # funkar för att ändra filtyp

if inp == 5:
    image_name = Image.open("pic.jpg")
    # visar olika info
    print(image_name.size)
    print(image_name.filename)
    print(image_name.format)
    print(image_name.format_description)