#all

bool_set={True , True , True ,45, None }
print("all items are not true: ", not all(bool_set))

#any 
bool_set = {True,True,False}
print("if one element at least is valid: ", any(bool_set))

#all --> check if all items in a set are valid 

print(all({
    5==5 ,
    3 < 2, 
    5 is 5
}))

print (
    5 == 5 and 3 < 2
)

n1 = 65
n2 = 65

name1 = "rania"
name2 = "rania"

print (all({
    65 ==65 ,
    n1 is n2 ,
    name1 is name2
}))

#any --> check if at least one item is valid 

print(
    any({
        5 ==5,
        4 == 5
    })
)