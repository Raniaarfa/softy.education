#loop 4 times
#get name from input 
# save name fi file

names = []

for i in range(4):
    name = input("Enter a name: ")
    names.append(name+"\n")

name_file = open("./my_names.txt", "a")

name_file.writelines(names)

name_file.close()