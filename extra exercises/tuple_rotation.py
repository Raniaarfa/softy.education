n=int(input("write a positive number : \n"))
while n < 0 :
    n=int(input("the number is not positive ,try again :\n"))
t=[]
for i in range (4):
    t.append(int(input("write a number to create a tuple:")))

tuple=tuple(t)

def rotate(tuple):
    print('before rotation :\n')
    print ("tuple = ",tuple)
    
    print("After swap:\n")
    for i in range(0,len(tuple)):
        new_tuple=tuple[len(tuple)-1]
        i = i + n
    return(new_tuple)

rotate(tuple)
