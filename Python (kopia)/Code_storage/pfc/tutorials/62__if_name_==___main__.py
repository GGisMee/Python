# 62__if_name_==__main__.py
# två former där modulen/programmet antingen kan vara:
# main, alltså själva programmet
# eller ett bihang som importas och används i ett annat program, t.ex. css och js importing

# viktigt för att ge flexabilitet
# då man kan köra ett program som bihang eller som eget program beroende på "__if_name_==__main__"

if __name__ == "__main__":
    pass


# import 59__list_comprehensions
# if 59_list_comprhensions.__name__ == "__main__" print("It is") else print("It isn't")
