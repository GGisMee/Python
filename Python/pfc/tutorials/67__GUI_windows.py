# 67__GUI_windows
# funkerar genom thinker
# GUI för grafisk användar sida
from tkinter import * # importar allt

# widgets = GUI elements: knappar, textboxar, etiketter, biilder
# windows = container till widgetsarna

window = Tk() # skapar en window

icon = PhotoImage(file="") # ikon över bilden, kräver att 
# window.iconphoto(True, icon)

window.geometry("400x400")
window.title("GGs first GUI program in PY, HTML kinda better tbh, still my thought tbh 2023 17 Mai")

window.config(background="blue") # kan också ha hexadecimal värde i färg (#) är viktigt

window.mainloop() # visar windown måste vara sist för att allt ska visas

