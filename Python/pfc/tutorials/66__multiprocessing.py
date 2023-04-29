# 66__multiprocessing
# är när man kör flera tasks samtidigt som är väldigt stora och kan bara köra 1 parallel task under tiden.
from multiprocessing import Process, cpu_count
import time

info = 0
def counter(num, info):
    count = 0
    while count < num:
        count += 1


if __name__ == '__main__': # krävs för att det ska funka
    x = int(input("hur många 10 potenser?: "))
    y = input("Ex (1,2,3):")
    print(10**x)
    if y == 1:
        a = Process(target=counter, args=(10**x,)) 
        a.start()
        a.join()
    if y == 2:

        a = Process(target=counter, args=(int((10**x)/2), )) # jämfört med 1 så är denna effektivare då den -
        b = Process(target=counter, args=(int((10**x)/2), )) # fördelar arbetet

        a.start()
        b.start()

        a.join()
        b.join() 
    
    # gör att vi istället för att köra en i taget kör alla samtidigt

    print("finished in "+str(time.perf_counter()))
    print(info)