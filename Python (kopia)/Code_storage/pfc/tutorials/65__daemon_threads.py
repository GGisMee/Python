# 65__daemon_threads
# mini thread som körs i bakgrunden, kan ej bli avstängd och fortsätter existera till programmet är slutkört

# användning: bakgrunds jobb, garbage collection, väntan på input, långa processer.
import threading
import time

def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        if count == 1:
            print("\n")
        print("logged in for: ", count, "secounds")
        


inp = int(input("Ex (1,2)"))

if inp == 1:
    threading.Thread(target=timer).start()
if inp == 2:
    threading.Thread(target=timer, daemon=True).start() # daemon=True, gör att Threaden inte cancelar main thread utan är mer i bakgrunden
    # x.setDaemon(True funkar också fast innan man aktiverar)

# för att ändra deamon senare, så kan du använda 

answer = str(input("Do you wish to exit?"))
print("done")
if answer != "":
    print("Answer here: "+answer)
    print("something")
    exit()
    

