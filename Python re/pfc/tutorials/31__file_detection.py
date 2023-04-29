# 31__file_detection
import os
path = "/Users/gustavgamstedt/PycharmProjects/programmering/Python/till main/till fil 31 folder"  # en folder
path = "/Users/gustavgamstedt/PycharmProjects/programmering/Python/till main/till fil 31 fil" # en fil
if os.path.exists(path):
    if os.path.isfile(path):
        print("Its a file")
    elif os.path.isdir(path):
        print("That is a folder!")
else:
    print("That location does not exist")
