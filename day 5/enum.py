pets = {"cat", "cat" , "dog" , "hamster"}

for position ,pet in enumerate(pets):
    print("the pet ",pet , " has the position ", position)

print("\n")
pets = sorted(pets , reverse=True)
for position ,pet in enumerate(pets):
    print("the pet" , pet , "has the position ", position)

print("\n")

for position ,pet in enumerate(sorted(pets)):
    print("the pet" , pet , "has the position ", position)

#len
#sorted
#min
#max
print ("\n")
print("the lenght of the set : " , len(pets))
print("\n")
numbers = {4, 44 ,12}
print("the max of numbers is", max(numbers) )
print("the min of numbers is", min(numbers))