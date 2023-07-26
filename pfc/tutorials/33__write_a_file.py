# 33__write_a_file
text = "Hallååååå \n Detta är ett meddelande som ska displayas i en text"  # \n delar upp ett print meddelande liknande ‹br›.
# denna skulle kunna användas för att redigera meddelanden liksåväl!
with open("till fil 33.txt", "w") as file: # w står för write, r för read, a för append eller lägg till
    file.write(text)
    file.write("Yee \n some extra text") # d