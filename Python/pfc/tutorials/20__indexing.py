# 20__indexing
name = "Gustav Gamstedt"
if(name[1].islower()):
    name = name.capitalize()

first_name = name[:6].upper()
last_name = name[7:].lower()
last_character = name[-2:] # om man vill få den sista bokstaven i en fras alltså i detta fallet t så kan man skriva -1 alltså gå under 0 värdet. Därefter kan man fortsätta och nå använda kolon som vanligt i minus skalan.
print(first_name +" "+ last_name)
print(last_character)
