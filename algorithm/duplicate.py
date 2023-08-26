
def duplicate(list, number):
    counter = 0

    for i in range (len(list)):
        if list[i] == number:
            counter = counter+1
    print("\nthe number is duplicated ", counter , "times\n")
    if counter == 0:
        print("Number Not in list !")    
    
        
list = [ 0, 9 ,6 , 6 ,8 ,0 ,17 , 4 , 23]
number = int(input("\nEnter a number :  "))
duplicate(list, number)