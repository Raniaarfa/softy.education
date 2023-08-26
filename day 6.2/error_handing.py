try:
    x = float(input("enter x :"))
    y = float(input("enter y :"))
    print(x/y)
except ZeroDivisionError :
    print("we can't divide by zero!")

except ValueError:
    print ("x or y should be a number! ")
    
else :
    print("it works only if there is no error!")
finally :
    print("Always works")

#expect float input