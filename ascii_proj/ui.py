import tkinter as tk
from tkinter import PhotoImage, filedialog
from PIL import Image, ImageTk
from getAscii import getAsciiData
# Create the main window
window = tk.Tk()
window.title('Ascii Converter')
root = tk.Frame(window)
root.pack()

char_var=tk.StringVar()

# Declare image as a global variable outside the function
image = None

def button_clicked():
    # Access the image stored in the label
    if image_label.image is not None:
        print("Image reference:", image_label.image)
        pil_image = ImageTk.getimage(image_label.image)
        PixelsX = slider1.get()
        PixelsY = slider2.get()
        
        getAsciiData(pil_image, PixelsX, PixelsY)
        

    else:
        print("No image loaded.")

def import_file():
    global image  # Use global to modify the global image variable
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Got file: {file_path}")

        image = Image.open(file_path)
        
        # Resize the image to the desired size (for example, 200x200)
        img_width, img_height = image.size
        percentage = 200 / img_width
        image = image.resize((200, round(percentage * img_height)), Image.ANTIALIAS)
        
        # Create PhotoImage from the resized image
        photo_image = ImageTk.PhotoImage(image)
        
        # Update the image label with the new image and store the reference
        image_label.config(image=photo_image)
        image_label.image = photo_image  # Keep a reference to avoid garbage collection
        window.update()

# Create UI elements
import_label = tk.Label(root, text='Import picture below')
import_label.pack()
import_button = tk.Button(root, text="Import File", command=import_file)
import_button.pack()

# Create the image label outside the function so it can be updated later
image_label = tk.Label(root)
image_label.pack()

x_label = tk.Label(root, text='Insert number of characters in x')
x_label.pack()
slider1 = tk.Scale(root, from_=1, to=300, orient=tk.HORIZONTAL)
slider1.pack()

slider2 = tk.Scale(root, from_=1, to=300, orient=tk.HORIZONTAL)
slider2.pack()

CharLabel = tk.Label(root,text='Insert ascii characters from blackest to whitest, ex: "░▒▓█"')
CharLabel.pack()

Char_entry = tk.Entry(root,textvariable = char_var, font=('calibre',10,'normal'))
Char_entry.pack()


button = tk.Button(root, text="Get Ascii", command=button_clicked)
button.pack()



window.mainloop()
