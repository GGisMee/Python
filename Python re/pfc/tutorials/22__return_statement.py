# 22__return_statement
def multiplication(nummer_1, nummer_2):
  return nummer_1 * nummer_2 # återlämnar kunskapen

x = multiplication(6,8)
print(x)

# annars
def multiplikation(number_1, number_2):
  number_1 * number_2 # återlämnar kunskapen

y = multiplikation(6,8)
print(y)

# alternativ lösning
def multiplikation(number_1, number_2):
  global y
  y = number_1 * number_2 # återlämnar kunskapen

multiplikation(6,8)
print(y)