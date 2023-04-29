# 13__nested_loops
rader = int(input("hur många rader: "))
bredd = int(input("hur brett: "))
bokstav = input("bokstaven: ")
for i in range(bredd):
    for j in range(rader):
        print(bokstav, end="")
    print()
