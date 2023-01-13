alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ""ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
dechiffering_eller_chiffering = input("Vill du Chiffera eller inte, skriv inget om du vill chiffera?: ")
meddelande_text = input("Skriv ditt meddelande som ska krypteras här: ").upper()
if dechiffering_eller_chiffering == "":
    nyckel = int(input("Ange det tal mellan 1 och 28 som ska vara din nyckel till meddelandet: "))
else:
    nyckel = int(input("Ange det tal mellan 1 och 28 som ska vara din nyckel till meddelandet: "))
    nyckel = nyckel - nyckel*2



krypteradstrang = ""
for aktuellt_tecken in meddelande_text:
    position = alfabet.find(aktuellt_tecken)
    nyPosition = position + nyckel
    if aktuellt_tecken in alfabet:
        krypteradstrang = krypteradstrang + alfabet[nyPosition]
    else:
        krypteradstrang = krypteradstrang + aktuellt_tecken
print("Det krypterade meddelandet är: ", (krypteradstrang).lower())
