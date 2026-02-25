#find largest number in diffrent 3 numbers
i = int(input("enter first number:"))
j = int(input("enter second number:"))
k = int(input("enter third number:"))
if(i>=j and i>=k):
    if(i==j==k):
        print("all number are same")
    elif(i==j and i>k):
        print("first two numbers are same & larger")
    elif(i==k and i>j):
        print("first and last number are same & larger")
    else:
        print("first number is largest number")
elif(j>=k):
    if(j==k):
        print("last two number are same & larger")
    else:
        print("second number is largest number")
else:
    print("third number is largest number")