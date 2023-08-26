import json
import os

#create a dict that has:
#-->name
#-->email
#-->age
#--> class

data ={
    "name":input("Enter your name = "),
    "email":input("Enter your gmail = "),
    "age": input("Enter your age = "),
    "class":input("Enter your class = ")
}

#save it in json file
working_directory = os.getcwd()
project_path =os.path.join(working_directory,"project")
contact_json_file=os.path.join(project_path,data['name']+".json")

with open(contact_json_file,'w') as contact_file:
    contact_str=json.dumps(data)
    contact_file.write(contact_str)

print("File successfuly created !")