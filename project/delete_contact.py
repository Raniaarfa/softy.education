import os 

working_directory = os.getcwd()
project_path = os.path.join(working_directory,"project")

conact_name = input("Enter the name : ")
json_file_name  = conact_name +".json"
json_file_path =  os.path.join(project_path , json_file_name)

if os.path.exists(json_file_path):
    os.remove(json_file_path)
    print(json_file_name + "has been deleted ")
else:
    print("File do not exist !")