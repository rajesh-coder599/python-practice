#find even & odd
i = int(input("enter number: "))
if (i%2==0):
    print("even")
else:
    print("odd")

#print the revers of string
str1 = "modi"
revers = ""
for i in str1:
    revers = i + revers


print(revers)

#find max & minimum from list
list1 = [1,2,3,4]
mx = list1[0]
mn = list1[0]
for i in list1:
    if(i>mx):
        mx=i
    if(i<mn):
        mn=i
print(mx)
print(mn)

#find if number is prime or not
num1 = -6
if(num1<=1):
    print("number is not prime")
else:
    for i in range(2,int(num1**0.5)+1):
        if(num1%i==0):
            print("number is not prime")
            break
    else:
        print("number is prime")

#count vowels in any string
str2 = "rajesh"
vowels = "aeiouAEIOU"
count=0
for i in str2:
    if(i in vowels):
        count+=1
print(count)