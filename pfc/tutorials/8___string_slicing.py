# 8___string_slicing
name = "Gustav Gamstedt"
# indexing[] or slice()
# [start:stop:step]
first_name = name[0]
first_name = name[:6]
last_name = name[7:]
print(first_name + " " + last_name)
konstigt_namn = name[0:6:2]
print(konstigt_namn)
reversed_name = name[::-1]
print(reversed_name)

print("----------------------------------------------------")
website = "https://www.youtube.com/watch?v=XKHEtdqhLK8"
website2 = "https://wikipedia.com"
slice2 = slice(8, -4)
print(website2[slice2])