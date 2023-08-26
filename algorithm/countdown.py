def countdown(n):
    while (n >= 1):
        print(n)
        n=n-1
n = int (input("Enter a number :  "))
countdown(n)

#recursion
def countdown(n):
    #base case
    if n == 0:
        return #exit function
    print(n)
    countdown(n-1)
n = int(input("enter n :  "))
countdown(n)
