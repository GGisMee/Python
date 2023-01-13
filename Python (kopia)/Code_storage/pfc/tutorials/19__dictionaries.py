# 19__dictionaries
capitals = {"USA":"Washington DC", # som en sammankoppling mellan en nyckel och ett ord
           "India":"New Delhi",
           "China": "Beijing",
           "Sweden":"Västerås"}
print(capitals["USA"]) # för att få ut ett värde med en nyckel
print(capitals.get("germany")) # för att genomsöka om en nyckel finns
print(capitals.keys()) # bara nycklarna
print(capitals.values())
print(capitals.items())
for i in capitals.values(): # alternativ lösning nedan
    capitals.update({"Germany":"Berlin"}) # lägg till ett nytt value och nyckel
    capitals.update({"USA":"New York"}) # ändra valuet
    capitals.pop("USA") # Ta bort, med value samtidigt som nyckel
    capitals.clear() # ta bort allt
for key, value in capitals.items():
    print(key, value)
