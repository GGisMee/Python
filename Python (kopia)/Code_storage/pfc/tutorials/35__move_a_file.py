# 35__move_a_file
import os
source = "till main/till fil 35.txt"  # vad som ska flyttas
destination = "/Users/gustavgamstedt/Desktop/till fil 35.txt"  # vart den ska flyttas
text = "Hej denna filen ska flyttas till desktop.\nEfter att först ha skapats i ''till main'' "

try: #för att skapa filen här nedan
     with open("till main/till fil 35.txt", "w") as file:
         file.write(text)
except FileNotFoundError:
    print("Source not found")
print()
try: # för att flytta filen här nedan
    if os.path.exists(destination):
         print("There is already a file there")
    else:
        os.replace(source,destination) # ett sätt att byta ut
        print(source+" was moved")
except FileNotFoundError:
    print("Source not found")
