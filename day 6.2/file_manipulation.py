# 1- OPEN FILE
names_file = open(
    r"/Users/selmi/Desktop/softy-education/day6/names.txt",
    'r'
)

# 2- READ FILE CONTENT
#content = names_file.read()
lines = names_file.readline()

# 3- MANIPULATION
#print("content : \n ", content )
print(lines)

# 4- CLOSE
names_file.close()