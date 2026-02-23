#file I/O
#python can be used to perform operations on a file

#open read & close the file
f = open("file.txt","r") #syntax "file name","mode(default=r)"
data = f.read()#read the data
print(data)
f.close() #imp, as a responsible programer we have to close file after our work is done
