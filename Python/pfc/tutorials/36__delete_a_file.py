# 36__delete_a_file
import os
text = "Hello this file doesn't exist anymore hehehhe after run"
try: #för att skapa filen här nedan
   with open("till main/till fil 36.txt", "w") as file:
      file.write(text)
except FileNotFoundError:
   print("Source not found")
input()

try: #för att skapa filen här nedan
    os.remove("till main/till fil 36.txt")
except FileNotFoundError:
    print("Source not found")
print()
