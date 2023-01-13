# 30__exception_handling
try:  # try kan användas för att testa en del där error kan uppstå
    taljare = float(input("Vilken är din täljare?: "))
    namnare = float(input("vilken är din nämnare?: "))
    resultat = taljare / namnare
    print(resultat) # om man väljer nämnaren som noll blir det ett error
except ZeroDivisionError as e: # därför krävs exceotion
    print("You cant devide by zero! " + str(e))
except ValueError as e:
    print("The input has to be a value " + str(e))
except Exception as e:  # exception visar vad som ska göras om error uppstår. i detta fallet alla errors fördelen är att man nu kan köra igen med en while loop och be om ny inmatning
    print("something went wrong" + str(e))
else: # else kan användas efter exceptions såväl som i if statements.
    print(resultat)
finally: # görs alltid
    print("This will always execute")
