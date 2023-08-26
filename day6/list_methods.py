movies=["avatar","mean girls","wild child","clueless","avatar",]

print("i watched",movies.count("avatar"),"avatar.")

print("\nprint movies with reverse()\n")
movies.reverse()
print(movies)

#pets.reverse()
#pets =pets [::-1]
print("\n\nprint movies with sorted reverse\n")
print(sorted(movies, reverse=True))

#pop
movies.pop()
movies.pop(2)
print (movies)

for i in range(len(movies)):
    movies.pop(i)
print(movies)