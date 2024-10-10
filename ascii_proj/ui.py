import tkinter as tk
from tkinter import PhotoImage, filedialog
from PIL import Image, ImageTk
window = tk.Tk()
window.title('Ascii Converter')
root = tk.Frame(window)
root.pack()

# Deklarera image som en global variabel utanför funktionen
image = None

def import_file():
    global image  # Använd global för att ändra den globala variabeln image
    file_path = filedialog.askopenfilename()
    if file_path:
        # Process the selected file (you can replace this with your own logic)
        print(f"got file: {file_path}")

        image = Image.open(file_path)
        
        # Ändra storlek på bilden till önskad storlek (exempelvis 200x200)
        image = image.resize((200, 200), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        image_label.config(image=image)  # Uppdatera bildetiketten med den nya bilden
        window.update()

import_button = tk.Button(root, text="Import File", command=import_file)
import_button.pack(pady=100)

# Skapa bildetiketten utanför funktionen så att den kan uppdateras senare
image_label = tk.Label(root, image="")
image_label.pack()

window.mainloop()
