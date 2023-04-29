# 27__**kwargs
# parameter som packar ihop alla argument till en dictionary
def hello(**kwargs): # samma som med args att man kan byta ut till vadsomhellst bara det är 2 stjärnor i det här fallet
   #print( "Hello "+kwargs["first_name"]+ " "+ kwargs["last_name"])
   print("hello", end=" ") # end för att inte hoppa ned en rad
   for key, value in kwargs.items():
       print(value, end=(" "))

hello( title="Mr",first_name="Gustav",middle_name="Paul", last_name="Gamstedt") # här heter first_name key och Gustav value
