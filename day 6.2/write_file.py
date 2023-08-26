#1- OPEN FILE
name_file =open(
    r"C:\Users\hp dm1\Documents\software craft\day 4\day 6.2\pets.txt",
    'a' #override
)

#write file content 
name_file.write("cats")
name_file.write("\ndogs")
name_file.write("\ncows")


#4- Close
name_file.close()