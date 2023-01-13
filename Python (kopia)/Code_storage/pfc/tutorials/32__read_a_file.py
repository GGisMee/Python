# 32__read_a_file
try:
    with open("/Python/Code_storage/pfc/till_library/till fil 32.txt") as file:
        fileinfo = file.read()
        print(fileinfo)
except FileNotFoundError:
    print("didn't find")

