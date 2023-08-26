import os

path_of_working_directory = os.getcwd()
list_of_folders = os.listdir(path_of_working_directory)
print(path_of_working_directory)

for file in list_of_folders :
    print(file)