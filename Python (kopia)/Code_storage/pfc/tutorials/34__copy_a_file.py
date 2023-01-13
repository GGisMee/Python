# 34__copy_a_file'
from shutil import copy, copy2, copyfile
# copyfile() # kopierar det som finns i en fil
# copy # kopierar allt som copyfile kopierar och kan koppiera mappar. samt permissions mode?!
# copy2() # kopierar även filens skapelse och modifierings tider

import shutil
shutil.copyfile("till main/till fil 33.txt", "till main/till fil 33 kopia.txt") # copyfile(vad som ska kopieras, kopians namn eller destination)
