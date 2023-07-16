# main float,int
def input_f():
    try:
        return int(input("Enter number: "))
    except ValueError:
        input_f()