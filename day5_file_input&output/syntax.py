with open("file.txt","r") as f:
    data = f.read()
    print(data) # with will close the file for as

with open("demmo.txt","a") as g:
    g.write("hello humans")
    