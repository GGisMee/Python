import random
from typing import List

kör = True
while kör == True:
    en_plats = ["på pluto", "i en läskig grotta", "på en trång skola", "vid stranden"]
    man = ["en polis","en luffare", "en pensionär", "en robot"]
    kvinna = ["En forskare", "En drottning", "Ett sto", "En präst"]
    honBar = ["en svart våtdräkt", "rosa änglavingar", "en svart sopsäck", "en snäv klänning"]
    hanBar = ["en lila sidenkostym", "ett älghuvud", "en prickig badhandduk", " en handduk"]
    honSa = ["Vem är du?", "Hur många ärtor äter du per dag?", "Men varför är du här?","Kom med till busken"]
    hanSa = ["Hej svejs", "Käka inte kråkor!", "självklart!", " Har du med dig en"]
    följd = ["fred på jorden", "de gjorde det", "kaos", "orkan"]
    världSa = ["Vilken nys!", "Ja det var skönt", "Jag smälter", "livet går vidare"]
    print("Hon hade på sig:", honBar[int(random.randint(0,3))])
    print("Han hade på sig:", hanBar[int(random.randint(0,3))])
    print()
    print("Hon sa", honSa[int(random.randint(0,3))])
    print("Han sa", hanSa[int(random.randint(0,3))])
    print("Följden blev:", random.choice(följd))
    print("Världen sa:", världSa[int(random.randint(0,3))])
    print()
    print()
    inputen = input("Tryck return för att fortsätta och något för att sluta:").lower()
    print()
if inputen == "stop":
        kör = False