fruit={
    "name": "orange",
    "weight":"10 Kg",
    "score" : 5
}

fruit.pop("score") #remove
fruit.update({"quality":"Good"}) #update
print(fruit)

print("All the keys!", fruit.keys())
print("All the values!", fruit.values())

print(fruit.get("name"))