# 37__modules
# att separera ett program i flera delar!
from Python.Code_storage.pfc.till_library import Till_37_module as T3M

T3M.hello() # behöver ej ha .hello om man inte vill aktivera definitionen
T3M.bye()
# Till_37_module # detta funkar desväl själv att aktivera
T3M # detta funkar även då man skrev om som T3M i import

help("modules") # modules är det som är efter import t.ex. math, random, os, turtle, Till_37_module mm
