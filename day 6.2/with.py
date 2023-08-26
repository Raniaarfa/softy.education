try:
    with open(r"C:\Users\hp dm1\Documents\software craft\day 4\day 6.2\names.txt", "r") as name_file:
        content = name_file.read()
        print(content)
except:
    print("")