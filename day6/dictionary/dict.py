fruit={
    "name": "orange",
    "weight":"10 Kg"
}
print(fruit)
print("the name of the fruit is ",fruit["name"])
print("the weight of the fruit is", fruit ["weight"])

print("the size of the fruit is :", len(fruit))

#update 
fruit["name"] = "Apple"
fruit["quality"] = "Good"
fruit["score"]= 5
print(fruit)

# delete
del fruit["score"]
fruit.clear() #empty the dictionary
print (fruit)