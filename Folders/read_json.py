import json
import os 

path_of_working_directory =os.getcwd()
path_of_os_folder = os.path.join(
    path_of_working_directory,
    "os"
)
os_folder_exists = os.path.exists(path_of_os_folder)
if(not os_folder_exists):
    os.mkdir(path_of_os_folder)

path_of_json_file = os.path.join(
    path_of_os_folder,
    "data.json"
)

with open(path_of_json_file.'r') as json_file: