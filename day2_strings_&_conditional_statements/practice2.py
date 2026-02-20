#WAP to input user's first name & print its length
a = input("enter your name: ")
b = len(a)
print("your name's length is: ", b)

#WAP to find the occurrence of $ in a string
str1 = input("input your string here to find occurence of $")
print("number of $ in your string is: ",str1.count("$"))

#WAP to check if a number entered by the user is odd or even
num = int(input("enter number"))
if(num%2 == 0):
    print("given number is even number")
else:
    print("given number is odd")

#WAP to find greatest of 3 numbers entered by the user
i = int(input("enter first number: "))
j = int(input("enter second number: "))
k = int(input("enter third number: "))
if((i>j) and (i>k)):
    print("first number is greatest number")
elif((j>i) and (j>k)):
    print("second number is greatest number")
elif((k>i) and (k>j)):
    print("third number is greatest number")
else:
    print("do not enter same number")

#WAP to check if number is a multiple of 7 or not
num1 = int(input("enter number: "))
if(num1%7 == 0):
    print("given number is multiple of 7")

else:
    print("given nmber is not multiple of 7")