# 55__sort
# finns i två former; för listor och andra som tuple t.ex.
if inp := int(input("lvl 1,2?: ")) == 1:
    students = ["Dude", "Chuck", "Dave", "Duddley", "Dino"]

    students.sort(reverse=True) # alfabetisk nu baklänges
    nl = ""
    for i in students:
        nl += f"{i} "

    print(nl)

    students_tuple = ("Dude", "Chuck", "Dave", "Duddley", "Dino")
    sorted_students_tuple = sorted(students_tuple, reverse=True) # , key=age funkar här om flera
    # över är funktionstyp

    nl2 = ""
    for i in sorted_students_tuple:
        nl2 += f"{i} "
    print(nl2)
else:
    students_li = [
        ("Dude", "F", 32), 
        ("Chuck", "A", 20), 
        ("Dave", "D", 12),
        ("Duddley", "B", 12),
        ("Dino", "C", 60)
    ]
    grade = lambda grades: grades[1]
    age = lambda ages: ages[2]
    students_li.sort(key=grade, reverse=True)
    students_li.sort(key=age, reverse=True)
    for i in students_li:
        print(i)
