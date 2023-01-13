# 58__reduce
# lägger ihop flera värden i en samling till ett värde
br = print

# utan reduce
letters = ["H", "E","L","L","O"]
letters_ = ""
for letter in letters:
    letters_ += letter
print(letters_)

from functools import reduce

reduction = lambda x, y: x+y
word = reduce(reduction, letters)
print(word)

# påverkar och lägger ihop 2 och 2 alltså först,
#(gång 1) h,e,l,l,o -> he,l,l,o
#(gång 2) he,l,l,o -> hel,l,o
#(gång 3) hel,l,o -> hell,o
#(gång 4) hell,o -> hello
br()
factor = [5,4,3,2,1]
factor_func = lambda factor1, factor2: factor1*factor2
tot_produkt = reduce(factor_func, factor)
print(tot_produkt)
