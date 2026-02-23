#create a new file "practice.txt" using python Add the following data in it:
with open("practice.txt","+w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using java.\n")
    f.write("I like programming in java.")
    data = f.read()
    print(data) #this will give blank space because pointer is at the end
