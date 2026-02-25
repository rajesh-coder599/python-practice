#take to numbers from user then find(sum, difference, product, division)
i = int(input("enter first number: "))
j = int(input("enter second number: "))
sum = i+j
if(i>j):
    difference = i-j
    if(j!=0):
        division = ("your cotient is:",int(i/j),"your remainder is:",i%j)
    else:
        division = ("can not divide by zero")
else:
    difference = j-i
    if(i!=0):
        division = ("your cotient is:",int(j/i),"your remainder is:",j%i)
    else:
        division = ("can not divide by zero")

product = i*j
print("sum of given number is:",sum)
print("difference of given number:",difference)
print("product of given number is:",product)
print("larger number divided by smaller number is:",division)