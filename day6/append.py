Kdrama =["revenat","goblin","18 again","snowdrop"]

#set.add()
#list

Kdrama.extend(["the glory","revenge of others"])
Kdrama.append("our beloved summer")
Kdrama.insert(
    0,
    "extraordinary you"
)
Kdrama.insert(
    3,
    "kill me heal me"
)
Kdrama[1]="the revenant 2" # update
Kdrama[5]="Snowdrop"
print(Kdrama)
print(sorted(Kdrama,reverse=True))