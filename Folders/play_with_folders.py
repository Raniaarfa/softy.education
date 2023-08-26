import os

Parent_path = os.getcwd()
current_path = os.path.join(Parent_path,"folders")
idk_path = os.path.join(current_path,"idk")
Rania_path = os.path.join(current_path,"Rania")

print("parents : ",Parent_path)
print("currents : ", current_path)

#create a new folder 
try :
    os.mkdir(idk_path)
except FileExistsError :
     print("we already have this folder ! ")

#create with your name 
try :
    os.mkdir(Rania_path)
except FileExistsError :
    print("we already have this folder ! ")