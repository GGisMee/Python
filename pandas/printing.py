def prints(*x, **y):
    x = list(x)
    print(x[0])
    try:
        for i in range(x[1]):
            print()
    except (TypeError, IndexError):
        print()

