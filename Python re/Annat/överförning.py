import shutil
import os
import random
in_pycharm_folder = "/Users/gustavgamstedt/PycharmProjects/programmering"
in_onedrive_folder = "/Users/gustavgamstedt/Library/CloudStorage/OneDrive-ABBGymnasiet/Programmeringsfoldern"
# number = str(random.randint(1, 10000))

# try:
#     os.rename(in_onedrive_folder, in_onedrive_folder + number)
#     in_onedrive_folder = in_onedrive_folder + number
# except FileNotFoundError:
#     print("change folder name manualy back without number")
# os.replace(in_onedrive_folder, "/Users/gustavgamstedt/Desktop/Programmering")
# shutil.copytree(in_pycharm_folder, in_onedrive_folder)
# print()

try:
    shutil.rmtree(in_onedrive_folder) # shutil.copytree(in_pycharm_folder, in_onedrive_folder)
except FileNotFoundError:
    print("No file found")
shutil.copytree(in_pycharm_folder, in_onedrive_folder)