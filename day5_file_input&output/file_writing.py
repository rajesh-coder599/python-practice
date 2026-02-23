i = open("file.txt","w") #w mode will overwrite the data
i.write("this is overwrited on priveous data")
i.close

j = open("file.txt","a") #a mode will add the data
j.write("\nthis is added line by python code")
j.close

k = open("demmo.txt","a") #if file does not exist this will creat new file
k.write("this file is created by human")
k.close