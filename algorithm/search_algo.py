
#Linear search

def search(list , element):
    position = None
    for i in range (len(list)):
        #print(list[i],element) #debugging
        if list[i] == element:
            position = i 
            break
        
    if position == None :
        print("Not found !")
    else :
        print ("Found " ,element, "at position ", position)

list = [7, 9 ,89 , 98 , 49 , 873, 8 ,12 , 23]
element = int(input("Enter a number to look for :  "))
search(list , element )

#while : my work
# def search(list , element):
#     position = None 
#     while element <= len(list):
#         for i in range (len(list)):
#             if list[i] == element:
#                 position = i 
        
#     if position == None :
#         print("Not found !")
#     else :
#         print ("Found " ,element, "at position ", position)

# list = [5, 9, 0 , 67 , 54 ,832 , 9 ,23]
# element = int(input("Enter a number to look for :  "))
# search(list , element )
