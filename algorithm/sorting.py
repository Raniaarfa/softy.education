numbers = [5, 90, 2, 1, 17]

def sort_numbers(list_of_numbers):
    n= len(list_of_numbers)
    
    for i in range (n):
        for j in range (n-1):
            if list_of_numbers[j] > list_of_numbers[j+1]:
                temp = list_of_numbers[j]
                list_of_numbers [j] = list_of_numbers[j+1]
                list_of_numbers[j+1]= temp
    return list_of_numbers

print("Before sorting :\n")
print(numbers)

print("\nAfter sorting : \n")
numbers = sort_numbers(numbers)
print(numbers)

# sorting in descending way the opposite of the first 
def sort_numbers(list_of_numbers):
    n= len(list_of_numbers)
    
    for i in range (n):
        for j in range (n-1):
            if list_of_numbers[j] < list_of_numbers[j+1]:
                temp = list_of_numbers[j]
                list_of_numbers [j] = list_of_numbers[j+1]
                list_of_numbers[j+1]= temp
    return list_of_numbers

print("\nBefore sorting the second time :\n")
print(numbers)

print("\nAfter sorting the second time : \n")
numbers = sort_numbers(numbers)
print(numbers)