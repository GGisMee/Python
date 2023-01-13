# 25__variable_scope
name = "Gustav"
def display_name():
    name = "Gamstedt"
    print(name) # om lokala siktet över togs bort skulle den printa globala siktet då den är underprioriterad,men ändå med

print(name)
display_name()

# om jag skriver name = "Gamstedt" här så kommer det att vara en globalt sikte då den står för all kåd.
print(name)# funkar inte utanför nu då name är ett lokalt sikte alltså inuti def. Funkar typ som i genvägar
