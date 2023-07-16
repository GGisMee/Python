# 59__list_comprehensions
# ett sätt att skapa en ny lista med mindre kåd
# kan likna en lambda funktion, men är enklare att läsa
# lista = [förändring, för item i samling] y = x for i in range(0, 10)
inp = int(input("exe (1,2): "))

if inp == 1:
    br = print
    # utan listcomprehention
    squares = []
    for item in range(1,11):
        squares.append(item**2)
    print(squares)
    br()

    squares_ = [i**2 for i in range(1,11)]
    print()

if inp == 2:
    # utan list comprehension
    students = [100,90,80,70,60,50,40,30,0]
    passed_students = list(filter(lambda student: student >= 60, students))
    print(passed_students)

    print()

    # med list comprehension
    students_ = [student for student in students if student >= 60]
    students__ = [student for student in students if student < 60]
    print(students_)
    print(students__)