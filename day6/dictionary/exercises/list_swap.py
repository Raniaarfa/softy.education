tuple_1 =[1,2,3]
tuple_2 =[4,5,6]

#--> t1 =(4,2,6)
#--> t2 =(1.5.3)

def swap(tuple1,tuple2):
    print('before swap:\n')
    print ("tuple 1 =" ,tuple_1)
    print("tuple 2 = ",tuple_2)

    print("After swap:\n")
    temp= tuple_1[0]
    tuple_1[0]=tuple_2[0]
    tuple_2[0]=temp

    temp=tuple_2[2]
    tuple_2[2]=tuple_1[2]
    tuple_1[2]=temp


    print("tuple 1",tuple_1)
    print("tuple 2",tuple_2)

swap(tuple_1,tuple_2)

#correction

# result
# list1 = [4, 2, 6]
# list2 = [1, 5, 3]


def swap_lists(list1, list2):
    print("Before swap: \n")
    print("list 1 ", list1)
    print("list 2 ", list2)

    print("\n\nAfter swap:\n")

    temp = list1[0]
    list1[0] = list2[0]
    list2[0] = temp

    temp = list1[2]
    list1[2] = list2[2]
    list2[2] = temp

    print("list 1 ", list1)
    print("list 2 ", list2)


list1 = [1, 2, 3]
list2 = [4, 5, 6]

swap_lists(list1, list2)
