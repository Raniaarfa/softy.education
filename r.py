#radline --> get the first line

with open (r"names.txt",'r') as file_name:
    first_line = file_name.readline()
    print(first_line)

#readlines -- > get all lines in a list

with open (r"names.txt","r") as file_name:
    all_lines = file_name.readlines()
    for postion ,line in enumerate(all_lines):
        print("the line number",postion,"is", line)
