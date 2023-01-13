# 63__time_module
import time
print(time.ctime()) # dag idag
print(time.ctime(time.time())) # samma
print(time.localtime()) # samma lokalt fast i set
print()
print(time.ctime(0)) # dag då datorn räknade tid ifrån, kallas epoch
print(time.ctime(1000000)) # ett tillfälle 1 milj sek efter (övre)
print()
print(round(time.time())) # tid sedan epoch i sek
print()

time_object = time.localtime()
time_object = time.gmtime() # universal time
print(time_object)
print()
local_time_variabel = time.strftime("%B, %d, %Y, %H:", time_object) # i ruta[0] kan man skriva in kod från pythons hemsida för att visa någon specifik data
# månad, datum, år, månadsnr
print(local_time_variabel)
print()
time_string = "20 April, 2020"
time_object_ = time.strptime(time_string, "%d %B, %Y") # skrivs nu i struktur
print(time_object_)
print()
print()
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string_ = time.asctime(time_tuple)
print(time_string_)
print()
print()
time_tuple_ = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string__ = time.mktime(time_tuple_)
print(time_string__)