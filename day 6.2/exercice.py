
#loop 4 times
#get name from input 
# save name fi file
for name in range (4):
    name=input("write a name :\n")


names=open("name.txt","w")
for i in range(4):
    name=input("donner un nom:")
    names.write(name)
    names.write("\n")
names.close()

names=open("name.txt","w")
list=[]
for i in range(4):
    name=input("donner un nom:")
    list.append(name+"\n")
names.writelines(list)
names.close()

