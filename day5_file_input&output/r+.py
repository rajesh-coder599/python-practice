# read overrite (pointer start)
a = open("file.txt","r+") #this will overwrite from starting
a.write("thor")
print(a.read())