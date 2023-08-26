#create a file with 'w' mode

with open (r"names.txt", 'w') as name_file:
    names =["Rania\n","Farah\n","Yassin\n","Ranim"]
    name_file.writelines(names)
    print("\nnames file created successfully!\n")

#read a file with 'r' mode

with open(r"names.txt",'r') as file_name:
    content=file_name.read()
    print(content)

#Append name with 'a' mode

with open(r"names.txt",'a') as file_name:
    file_name.write("\nmohammed")