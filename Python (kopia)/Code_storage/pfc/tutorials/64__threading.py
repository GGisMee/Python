# 64__threading
# Ett sätt att bestämma när olika kodstycken ska köras och hur de ska köras vid olika tillfällen

#två typer
# cpu bound = programet eller kodstycket körs efter påverkningar från datorn själv
# använd multiprocessing

# io bound = programet eller kodstycket körs efter t.ex. påverkning från användare
# använd miltithreading för att köra flera kodstycken samtidigt

import threading, time
print(threading.active_count()) # antalet kodstycken som körs samtidigt
print(threading.enumerate()) # lista över olika aktiva kodstycken, MainThread är threaden som kör main delen av programmet
x = 0
# ex på användning är att ha en thread som kontrollerar input till svar på ett quiz, medan en annan kontrollerar tiden med en countdown

inp = int(input("Ex (multiprocessing(1), multithreading(2)):"))

def study():
    time.sleep(2)
    print("Clothes on")

def drink_hot_Chocolate():
    time.sleep(3)
    print("Teeth brushed")

def eat_breakfast():
    time.sleep(5)
    print("Breakfast eaten")

def timer():
    while threading.active_count() > 2:
        global x
        x +=1
        time.sleep(1)
    if threading.active_count() == 2:
        print(x)

if inp == 1:
    eat_breakfast(), drink_hot_Chocolate(), study(),  # 10 sek för breakfast(5), Hot Chocolate(3), Study (2)
    # om man gör det samtidigt och multitaskar kan det gå fortare! Genom multithreading
    # då kan man flera threads samtidigt

if inp == 2:
    breakfastThread = threading.Thread(target=eat_breakfast, args=()) # för att lägga in argument kan man använda args
    breakfastThread.start()

    Hot_ChocolateThread = threading.Thread(target=drink_hot_Chocolate, args=()) # för att lägga in argument kan man använda args
    Hot_ChocolateThread.start()

    breakfastThread = threading.Thread(target=study, args=()) # för att lägga in argument kan man använda args
    breakfastThread.start()

    rand = threading.Thread(target=timer, args=())
    rand.start()

# join ska kunna användas för att de andra program ska vänta på att den ska bli färdig





