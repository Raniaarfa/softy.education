import json
import os
import pprint

working_directory = os.getcwd()
project_path =os.path.join(working_directory,"project")

#list all contact + get only json files
list_of__all_files =os.listdir(project_path)
list_of_json_files = []
for file in list_of__all_files:
    if file.endswith(".json"):
        path =os.path.join(project_path,file)
        list_of_json_files.append(path)

print(list_of_json_files)

#get all the content from the json files 
contacts =[]
for json_file in list_of_json_files :
    with open(json_file,'r') as f:
        content= f.read()
        contact =json.loads(content)
        contacts.append(contact)

# 1 -selection for the contact to update (search)
# 2 -update contact (dict)
# 3 -update json file

search_input = input(
    """
    Enter the name of the contact you want to update: 
    """
)
result = {}

for contact in contacts :
    if search_input in contact["name"]:
        result = contact

if (len(result)>0):
    #update 
    result["hobby"] = 'Drawing'
    path = os.path.join(project_path , result['name']+".json")
    with open(path, "w") as file_to_update:
        #conversion dict ---> str
        update_str = json.dumps(result)
        file_to_update.write(update_str)
        print("Contact has been updated !")
else:
    print("contact not Found !")
