width, height = 400, 500

print(f"innan {width, height}")

if i := 0 == 1:  # avstängd
    # för att byta plats på width och height
    temp = width  # temp för temporär sparbank
    width = height
    height = temp


width, height = height, width  # annat sätt att skriva där man  skriver det utan temporär sparare
print(f"efter {width, height}")
