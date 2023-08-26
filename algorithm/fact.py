result = 1

n= int(input("Enter thr number N :  "))

#using for loop
for i in range (1 , n+1):
    result = result*i

print(n , "! = ", result)

#using while loop
counter = 1
result = 1
n = int(input ("Enter the number n :"))

while counter <= n :
    result = result * counter
    counter += 1

print(result)

#recursion 

def factoriel(n):
    #base case
    if n ==1:
        return 1
    #recursive case
    return n * factoriel(n-1)

n= int(input("Enter the Number N :  "))
result = factoriel(n)
print(result)