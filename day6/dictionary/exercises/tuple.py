tuple_1 =(1,2,3)
tuple_2 =(4,5,6)

#--> t1 =(4,2,6)
#--> t2 =(1.5.3)

def swap(tuple1,tuple2):
    print('before swap:\n')
    print ("tuple 1 =" ,tuple_1)
    print("tuple 2 = ",tuple_2)

    print("After swap:\n")
    new_tuple1=(tuple_2[0],tuple_1[1],tuple_2[2])
    new_tuple2=(tuple_1[0],tuple_2[1],tuple_1[2])
    print("tuple 1",new_tuple1)
    print("tuple 2",new_tuple2)

swap(tuple_1,tuple_2)