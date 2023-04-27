# 21__functions
def hello(namn, ålder, wow): # detta är själva funktionen och kan skrivas med def och sedan valfritt ord
    print("hello " + namn + " som är " + str(ålder) + " " + wow) # därefter fungerar den som andra tilljängligheter med en om då del
    print("have a nice day")
namn = "Gustav"
ålder = 16 # under spelar ordningen roll alltså kan inte "coolt" vara före ålder för då skulle koden inte förstå
hello(namn, ålder, "coolt") # för att uppkalla funktionen skriver man ned funktiones ordet och sedan paranteser
