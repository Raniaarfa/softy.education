
def sum(n):
    s = 0
    for i in range (1 , n+1) :
         s +=i
    return s
n = int(input("Enter a number n : "))
result = sum(n)
print(result)

#recursion 

def sum2(n):
    #base case 
    if n == 1:
        return 1 
    return n + sum2(n-1)
n = int(input("Enter a number n : "))
result = sum2(n)
print(result)




#shortcut to select all and turn it in comment ctrl + k + c
#shortcut to select all remive  comment ctrl + k + u