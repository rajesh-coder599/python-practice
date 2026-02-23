f = open("file.txt","r")
data = f.read(5) #this will read only 5 charechter including space
print(data)

line1 = f.readline() #this will read a single line at a time
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
data1 = f.read()
print(data1)
line4 = f.readline()
print(line4) #we cant read file twice
f.close()