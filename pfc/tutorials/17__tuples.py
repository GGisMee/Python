# 17__tuples
student = ("Bro", 29, "male")

print(student.count("Bro")) # antal gånger av Bro
print(student.index("Bro")) #plats i tuple

for x in student:
   print(x)

if "Bro" in student: #In används för att något finnsi något annat
   print("Yes")
else:
   print("nope")