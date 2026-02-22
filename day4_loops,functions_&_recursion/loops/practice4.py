#WAP to find the sum of first n numbers(using while)
num = int(input("enter number: "))
i = 0
sum = 0
while i<=num:
    sum = sum+i
    i+=1
    
print("your number",num ,"sum is:",sum)

#WAP to find the factorial of first n numbers(using for)
factorial = 1
j=int(input("enter number:"))
for i in range(1,j+1):
    factorial = factorial*i
    print(i,"factorial is: ",factorial)