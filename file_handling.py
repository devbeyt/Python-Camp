read_file = open("readFile.txt","r")
print(read_file.read())
read_file.close()

#**************************************

read_file = open("readFile.txt","r")
for lines in read_file.readlines():
    print(lines)
read_file.close()

#*****************************

write_file = open("writeFile.txt","w")        # "w" method will overwrite the entire file.
write_file = open("writeFile.txt","a")
write_file.write("3-Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,")
