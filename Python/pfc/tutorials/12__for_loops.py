# 12__for_loops
# skillanden är att for visar ett fixerat antal repititioner medan while inte gör det
from random import choices
"""
for index in range(10):
   print(index)

for index in range(10, 50):
   print (index + 1)

for index in range(10, 50 , 2):
   print("number: " + str(index))
"""

if input("Namndelning? Ja?: ").lower() == "ja":
    Namn = input("Vad heter du: ")
    for i in Namn: #alt lösning i istället för index. Index är som ett fixerat namn för något
        print(i)

if input("eggtimmer? Ja?: ").lower() == "ja":
    eggtimer = input("Hur länge ska egget koka? ")

    import time
    for seconds in range(int(eggtimer), 0, -1):
        print(seconds)
        time.sleep(1)
    print("now")

if input("Textremoval? Ja?: ").lower() == "ja":

    lista_over_tasbort = []


    avslutning_hmm = "None"
    while "*" not in avslutning_hmm :
        avslutning_hmm = input("Skriv in tecken en och en eller i grupp som ska tas bort. Avsluta med *: ")
        if "*" not in avslutning_hmm:
            lista_over_tasbort.append(avslutning_hmm)
    Editas = input("Det som ska redigeras: ")

    for char in lista_over_tasbort:
        sluttext = Editas.replace(char, "")
        print(sluttext)