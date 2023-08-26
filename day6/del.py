Kdrama =["revenat","goblin","18 again","snowdrop"]

print("before delete:\n")
print(Kdrama)

print("\n\nAfter delete:\n")
del Kdrama[0]
del Kdrama[-1]
#challenge : delete goblin
#del Kdrama [Kdrama.index("goblin")]

#update
Kdrama [Kdrama.index("goblin")]="DP" #remove
Kdrama.remove("18 again")
print(Kdrama)