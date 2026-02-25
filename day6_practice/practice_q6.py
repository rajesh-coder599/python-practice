#input user's marks & print his grade
i = float(input("enter your overall marks: "))
if(i>=90):
    print("your grade is A")
elif(i>=75):
    print("your grade is B")
elif(i>=60):
    print("your grade is C")
else:
    print("fail")